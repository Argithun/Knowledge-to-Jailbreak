import os
import pandas as pd
import numpy as np
import argparse
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import logging
from tqdm import tqdm
from configs import modeltype2path
import warnings
import json


logging.basicConfig(level=logging.INFO)
warnings.simplefilter("ignore")

DEFAULT_SYSTEM_PROMPT = """<<SYS>> You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Please ensure that your responses are socially unbiased and positive in nature. If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information. <</SYS>> """


def prepend_sys_prompt(sentence, args):
    if args.use_system_prompt:
        sentence = DEFAULT_SYSTEM_PROMPT + sentence
    return sentence


def get_sentence_embedding(model, tokenizer, sentence):
    sentence = sentence.strip().replace('"', "")
    word_embeddings = model.get_input_embeddings()

    # Embed the sentence
    tokenized = tokenizer(sentence, return_tensors="pt", add_special_tokens=False).to(
        model.device
    )
    embedded = word_embeddings(tokenized.input_ids)
    return embedded


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--model", type=str, help="which model to use", default="Llama-2-7b-chat-hf"
    )
    parser.add_argument(
        "--n_sample",
        type=int,
        default=1,
        help="how many results we generate for the sampling-based decoding",
    )
    parser.add_argument(
        "--prompt_type",
        default = 'original_prompt'
    )
    parser.add_argument(
        "--subjects",
        nargs='+'
    )
    parser.add_argument(
        "--use_greedy", action="store_true", help="enable the greedy decoding"
    )
    parser.add_argument(
        "--use_default", action="store_true", help="enable the default decoding"
    )
    parser.add_argument(
        "--tune_temp", action="store_true", help="enable the tuning of temperature"
    )
    parser.add_argument(
        "--tune_topp", action="store_true", help="enable the tuning of top_p"
    )
    parser.add_argument(
        "--tune_topk", action="store_true", help="enable the tuning of top_k"
    )

    parser.add_argument(
        "--use_system_prompt", action="store_true", help="enable the system prompt"
    )
    parser.add_argument(
        "--use_advbench",
        action="store_true",
        help="use the advbench dataset for evaluation",
    )
    args = parser.parse_args()

    model_name = modeltype2path[args.model]

    WEIGHTS_PATH = model_name
    TOKENIZER_PATH = WEIGHTS_PATH

    fname = args.model
    # if args.use_system_prompt:
    #     fname += "_with_sys_prompt"
    # if args.n_sample > 1:
    #     fname += f"_sample_{args.n_sample}"
    # if args.use_advbench:
    #     fname += "_advbench"
    if not os.path.exists(f"outputs/{fname}"):
        os.makedirs(f"outputs/{fname}")

    # if "falcon" in args.model or "mpt" in args.model:
    #     model = AutoModelForCausalLM.from_pretrained(
    #         WEIGHTS_PATH,
    #         torch_dtype=torch.bfloat16,
    #         trust_remote_code=True,
    #         low_cpu_mem_usage=True,
    #         device_map="auto",
    #     )
    # else:
    #     model = AutoModelForCausalLM.from_pretrained(
    #         WEIGHTS_PATH,
    #         torch_dtype=torch.float16,
    #         low_cpu_mem_usage=True,
    #         device_map="auto",
    #     )

    # tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)

    # logging.info(f"Model size: {model.get_memory_footprint()/1e9}")
    # logging.info(f"Model name: {fname}")

    lines = list()

    # with open("./data/MaliciousInstruct.txt") as f:
    # with open("../../all_test.json") as f:
    #     data = json.load(f)
    #     sub_list = args.subjects
    #     ptype = args.prompt_type
    #     for item in data:
    #         if item['subject'] in sub_list:
    #             lines.append(item[ptype])   #TODO

    # prepend sys prompt
    # lines = [prepend_sys_prompt(l, args) for l in lines]

        # logging.info(f"Running default, top_p=0.9, temp=0.1")
    outputs = list()
    
    with open("../../res_" + fname + "_chem.json", "r") as json_file:
        data = json.load(json_file)
        prompt_to_res = {}
        ptype = args.prompt_type
        for item in data:
            lines.append(item[ptype])
            outputs.append(item[ptype+'_response'])

    results = pd.DataFrame()
    results["prompt"] = lines
    results["output"] = outputs
    results.to_csv(f"outputs/{fname}/output_{args.prompt_type}_{str(args.subjects)}_chem.csv")

if __name__ == "__main__":
    main()
