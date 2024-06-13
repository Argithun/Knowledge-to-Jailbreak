import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ['TOKENIZERS_PARALLELISM'] = "false"

ALPHA_FOR_EIGEN_SCORE = 1e-3

import argparse
import pandas as pd
from tqdm import tqdm
import numpy as np
from io import StringIO
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import torch.nn.functional as F
from collections import Counter

from rouge_score.rouge_scorer import RougeScorer
rouge_scorer = RougeScorer(['rougeL'], use_stemmer=True)
rouge_fn = lambda target, pred: rouge_scorer.score(target, pred)['rougeL'].fmeasure
    
def compute_perplexities(logits: torch.tensor, input_ids: torch.tensor):
    assert logits.shape[:2] == input_ids.shape
    log_probs = F.log_softmax(logits, dim=-1)
    target_prob = torch.gather(log_probs, dim=-1, index=input_ids.unsqueeze(-1)).squeeze(-1)
    return torch.nanmean(-target_prob, dim=1).tolist()

def compute_energy_score(logits):
    log_sum_exp = torch.logsumexp(logits, dim=-1)
    return torch.nanmean(log_sum_exp, dim=1).tolist()

def compute_eigen_score(z:torch.tensor, alpha: float=ALPHA_FOR_EIGEN_SCORE):
    k,d = z.shape
    j_d = torch.eye(d) - (1/d) * torch.ones(d, d)
    sigma = torch.einsum('ij,jk,kl->il', z, j_d, z.t()) # 原论文里的z是d*K的，这里是K*d的，所以这里的z.t()是d*K的
    return ((1/k) * torch.logdet(sigma + alpha * torch.eye(k))).item()

def manual_check_sentence(sentence):
    if not sentence.strip():
        return False
    if "Q: " in sentence:
        return sentence.split("Q: ")[0]
    else:
        return sentence
    
def find_common_prefix(sequences):
    common_prefix = []
    for i in range(min(len(seq) for seq in sequences)):
        current = sequences[0][i]
        if all(seq[i] == current for seq in sequences):
            common_prefix.append(current)
        else:
            break
    return common_prefix

def compute_uncertainty(df, model, tokenizer, dataset_name):
    
    total_prompts = list(df['prompt'])
    total_prompts_ids = tokenizer(total_prompts, padding=False)['input_ids']
    common_prefix_ids = find_common_prefix(total_prompts_ids)
    common_prefix_kv = model(input_ids=torch.tensor([common_prefix_ids])).past_key_values

    new_df = pd.DataFrame(columns=[
        "id", "perplexity", "ln_entropy", "energy_score", "eigen_score", "lexical_similarity",
        "rouge_correctness", "similarity_correctness"
    ])

    for i, row in tqdm(df.iterrows(), total=len(df), desc=f"Calculating uncertainty for {dataset_name}"):
        # prepare inputs
        p_ids = total_prompts_ids[i]
        responses = [row['greedy_response']]+list(row['sampling_response'].keys())
        if len(responses) == 0 or not any(responses):
            print(f"Skipping row {i} as there are no responses")
            continue
        full_sentences = [f"{total_prompts[i]}{r}{tokenizer.eos_token}" for r in responses]
        full_sentences_encoded = tokenizer(full_sentences, return_tensors="pt", padding=True)

        # forward prompt
        prompt_encoded = {
            'input_ids': torch.tensor([p_ids[len(common_prefix_ids):]]),
            'past_key_values': common_prefix_kv,
            'attention_mask': torch.ones(1, len(p_ids), dtype=torch.long) # we need to send the full length of the prompt
        }
        prompt_output = model(**prompt_encoded)

        # forward responses
        batch_size = len(responses)
        batched_prompt_pkv = [(k.repeat(batch_size, 1, 1, 1), v.repeat(batch_size, 1, 1,1)) for k, v in prompt_output.past_key_values]
        full_sentences_encoded['input_ids'] = full_sentences_encoded['input_ids'][:, len(p_ids):]
        full_sentences_output = model(**full_sentences_encoded, past_key_values=batched_prompt_pkv, output_hidden_states=True)

        # post-process the logits and hidden states
        prompt_length = len(p_ids)
        ## logits for predicting next token
        answer_logits =  torch.cat(
            [prompt_output.logits[:,-1,:].repeat(batch_size, 1, 1), full_sentences_output.logits[:, :-1, :]], 
            dim=1
        )
        # mask the logits at padding
        attention_mask = full_sentences_encoded['attention_mask'][:, prompt_length:]
        extended_mask = torch.cat([attention_mask, torch.zeros(attention_mask.shape[0], 1, dtype=torch.long)], dim=1)
        shifted_attention_mask = extended_mask[:, 1:]
        answer_logits = answer_logits.masked_fill(~shifted_attention_mask.bool().unsqueeze(-1), float('nan'))

        perplexities = compute_perplexities(answer_logits, full_sentences_encoded['input_ids'])
        if not row['greedy_response']: # if the greedy response is empty, set the perplexity to a very high value
            perplexities[0] = 1000 
        sample_responses, sample_perplexities = [], []
        for r, p in zip(responses[1:], perplexities[1:]):
            if np.isnan(p):
                print(f"row {i}: Perplexity for response {r} is nan")
                continue
            sample_responses.append(r)
            sample_perplexities.append(p)
        if not sample_responses:
            print(f"Skipping row {i} as there are no valid responses")
            continue
        
        weights = [row['sampling_response'][r] for r in sample_responses]
        # logits based metrics
        perplexity = perplexities[0]
        ln_entropy = np.average(sample_perplexities, weights=weights)
        energy_score = compute_energy_score(answer_logits)
        energy_score = np.average(sample_perplexities, weights=weights)

        # hidden states based metrics
        layer = model.config.num_hidden_layers // 2 - 1
        eos_indices = attention_mask.sum(dim=1) - 1
        eos_hidden_states = full_sentences_output.hidden_states[layer][range(batch_size), eos_indices]
        eos_hidden_states = eos_hidden_states[1:, :] # remove the greedy generation
        eos_hidden_states = torch.cat(
            [eos_hidden_states[i].repeat(weights[i], 1) for i in range(len(weights))], 
            dim=0
        )
        eigen_score = compute_eigen_score(eos_hidden_states)
        # append to the new dataframe
        index_to_append = len(new_df)
        new_df.loc[index_to_append, 'id'] = row['id']
        new_df.loc[index_to_append, 'perplexity'] = perplexity
        new_df.loc[index_to_append, 'ln_entropy'] = ln_entropy
        new_df.loc[index_to_append, 'energy_score'] = energy_score
        new_df.loc[index_to_append, 'eigen_score'] = eigen_score
        new_df.loc[index_to_append, 'rouge_correctness'] = row['rouge_correctness']
        new_df.loc[index_to_append, 'similarity_correctness'] = row['similarity_correctness']

        # calculate the similarity
        lexical_similarity = compute_similarity_for_row(row['sampling_response'])
        new_df.loc[index_to_append, 'lexical_similarity'] = lexical_similarity
    return new_df

def compute_similarity_for_row(sampling_response: dict):
    sentences = list(sampling_response.keys())
    if len(sentences) < 2:
        return 1
    sentence_pair_counter = Counter()
    same_pair_cnt = 0
    for i, sentence in enumerate(sentences):
        same_pair_cnt += sampling_response[sentence] * (sampling_response[sentence] - 1) // 2
        for j in range(i+1, len(sentences)):
            sentence_pair_counter[(sentence, sentences[j])] = sampling_response[sentence] * sampling_response[sentences[j]]
    sentence_pair_counter['same'] = same_pair_cnt
    total_sims = total_pairs = 0
    for pair, cnt in sentence_pair_counter.items():
        similarity = rouge_fn(pair[0], pair[1]) if pair != 'same' else 1
        total_sims += similarity * cnt
        total_pairs += cnt
    return total_sims / total_pairs


def main():
    parser = argparse.ArgumentParser()
    # parser.add_argument("--model_name_or_path", type=str, default="/data2/tsq/WaterBench/data/models/llama-2-7b-chat-hf", help="The model name")
    parser.add_argument("--model_name_or_path", type=str, default="/data3/MODELS/llama2-hf/llama-2-13b-chat", help="The model name")
    parser.add_argument("--data_dir", type=str, required=True)
    args = parser.parse_args()

    model = AutoModelForCausalLM.from_pretrained(args.model_name_or_path, device_map="auto")
    model.eval()
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
    tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.padding_side = "right"

    file_suffix = "_correctness.jsonl"
    
    # ds_names = ["coqa", "nq", "squad", "triviaqa"]
    ds_names = ["waterbench", "nq1500"]
    # ds_names = ["waterbench"]

    for dataset_name in ds_names:
        file_path = os.path.join(args.data_dir, f"{dataset_name}{file_suffix}")
        print(f"Processing {file_path}")
        df = pd.read_json(file_path, orient="records", lines=True)

        if 'debug' in args.data_dir:
            df = df[:10]
        
        if dataset_name == "waterbench":
            # concat df[1000:] df[:1000]
            df = pd.concat([df[1000:], df[:1000]], ignore_index=True)
        with torch.no_grad():
            df = compute_uncertainty(df, model, tokenizer, dataset_name)

        save_path = os.path.join(args.data_dir, f"{dataset_name}_uncertainty.jsonl")
        df.to_json(save_path, lines=True, orient="records")
        print(f"Finished {dataset_name} to {save_path}")


if __name__=="__main__":
    main()