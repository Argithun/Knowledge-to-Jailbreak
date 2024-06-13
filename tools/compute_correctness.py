from metrics import rouge_and_similarity_score
import argparse
import os
import pandas as pd
from tqdm import tqdm

ROUGE_THRESHOLD = 0.5
SIMILARITY_THRESHOLD = 0.9

def compute_correctness(df, dataset_name):
    all_ground_truths, all_greedy_responses = [], []
    for i, row in df.iterrows():
        all_ground_truths.extend(row["ground_truth"])
        all_greedy_responses.extend([row["greedy_response"]]*len(row["ground_truth"]))
    rouge_scores, cosine_similarity = rouge_and_similarity_score(all_ground_truths, all_greedy_responses)
    correctness_iter = iter(zip(rouge_scores, cosine_similarity))

    # Initialize columns in df_output for the results
    df_output = df.copy()
    df_output['rouge'], df_output['rouge_correctness'], df_output['best_rouge_match'] = 0, False, ""
    df_output['cosine_similarity'], df_output['similarity_correctness'], df_output['best_similariy_match'] = 0, False, ""

    for i, row in df.iterrows():
        best_rouge, best_rouge_match, best_similarity, best_similarity_match = 0, "", 0, ""
        for gt in row["ground_truth"]:
            rouge, similarity = next(correctness_iter)
            if rouge > best_rouge:
                best_rouge, best_rouge_match = rouge, gt
            if similarity > best_similarity:
                best_similarity, best_similarity_match = similarity, gt
        df_output.loc[i, 'rouge'] = best_rouge
        df_output.loc[i, 'rouge_correctness'] = best_rouge > ROUGE_THRESHOLD
        df_output.loc[i, 'best_rouge_match'] = best_rouge_match
        df_output.loc[i, 'cosine_similarity'] = best_similarity
        df_output.loc[i, 'similarity_correctness'] = best_similarity > SIMILARITY_THRESHOLD
        if dataset_name == "waterbench":
            df_output.loc[i, 'misinfo_correctness'] = True
        else:
            df_output.loc[i, 'misinfo_correctness'] = False
        df_output.loc[i, 'best_similariy_match'] = best_similarity_match
        
    return df_output

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, required=True)
    args = parser.parse_args()

    # dataset_names = ['coqa', 'nq', 'squad', 'triviaqa']
    dataset_names = ["waterbench", "nq1500"]
    input_file_suffix = "_responses.jsonl"
    output_file_suffix = "_correctness.jsonl"

    for dataset_name in dataset_names:
        input_path = os.path.join(args.data_dir, f"{dataset_name}{input_file_suffix}")
        output_path = os.path.join(args.data_dir, f"{dataset_name}{output_file_suffix}")
        response_data = pd.read_json(input_path, orient="records", lines=True)
        print(f"Read {len(response_data)} responses from {input_path}")
        response_data = compute_correctness(response_data, dataset_name)
        response_data.to_json(output_path, orient="records", lines=True)
        print(f"Saved to {output_path}")


if __name__ == "__main__":
    main()