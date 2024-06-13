from easyjailbreak.selector.RandomSelector import RandomSelectPolicy
from easyjailbreak.datasets import JailbreakDataset, Instance
from easyjailbreak.seed import SeedTemplate
from easyjailbreak.mutation.rule import Translate
from easyjailbreak.models import from_pretrained
from sentence_transformers import SentenceTransformer, util
from easyjailbreak.metrics.Evaluator.Evaluator_ClassificationGetScore import EvaluatorClassificationGetScore
import torch
import json
import csv
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from heapq import nlargest
from tqdm import tqdm
from rank_bm25 import BM25Okapi


prompt_cannot_jailbreak = []
with open('./data/2_original_prompt_res_score.json', 'r') as json_file:
    for line in json_file:
        if line.strip() == "":
            continue
        try:
            item = json.loads(line.strip())
            if item['score'] < 2:
                prompt_cannot_jailbreak.append({"prompt": item['prompt_in_en'], "subject": item['subject']})
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            continue
    
QA_list = []

knowledge_path = "/data1/tsq/FactMark/src/DPR/downloads/data/wikipedia_split/psgs_w100.tsv"
num_lines = sum(1 for line in open(knowledge_path, 'r', encoding='utf-8'))
with open(knowledge_path, 'r', encoding='utf-8') as tsvfile:
    reader = csv.DictReader(tsvfile, delimiter='\t')

    for row in tqdm(reader, total=num_lines, desc="Reading wiki_en"):
        QA_list.append(row['text'])


tokenized_docs = [doc.split() for doc in QA_list]
bm25 = BM25Okapi(tokenized_docs)

with open('./data/3_prompt_and_knowledge.json', 'a') as json_file:
    for index, item in enumerate(tqdm(prompt_cannot_jailbreak, desc="Finding knowledge for prompts")):
        # 找到与 prompt 最相似的 top 50 个 knowledge
        scores = bm25.get_scores(item['prompt'].split())
        top_50_indexes = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:50]
        top_50_knowledge = [QA_list[idx] for idx in top_50_indexes]
        
        json.dump({'prompt': item['prompt'], 'subject': item['subject'], 'knowledge': top_50_knowledge}, json_file, ensure_ascii=False)
        json_file.write('\n')
