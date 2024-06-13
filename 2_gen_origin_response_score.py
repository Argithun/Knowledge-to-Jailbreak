from easyjailbreak.selector.RandomSelector import RandomSelectPolicy
from easyjailbreak.datasets import JailbreakDataset, Instance
from easyjailbreak.seed import SeedTemplate
from easyjailbreak.mutation.rule import Translate
from easyjailbreak.models import from_pretrained
from sentence_transformers import SentenceTransformer, util
from easyjailbreak.metrics.Evaluator.Evaluator_ClassificationGetScore import EvaluatorClassificationGetScore
from tqdm import tqdm 
import torch
import json
import os

model = from_pretrained('/data2/tsq/WaterBench/data/models/llama-2-7b-chat-hf', 
                        'llama-2', dtype=torch.bfloat16, max_new_tokens=200)
evaluator = EvaluatorClassificationGetScore(model)

# 定义文件路径
input_file_path = './data/1_original_prompt_with_response.json'
output_file_path = './data/2_original_prompt_res_score.json'

# 检查已处理的行数
processed_lines = 0
if os.path.exists(output_file_path):
    with open(output_file_path, 'r') as json_file:
        for line in json_file:
            processed_lines += 1

i = 0
# 遍历原始数据，提取 "response" 字段，并添加进度条
with open(input_file_path, 'r') as json_file_1, open(output_file_path, 'a') as json_file_2:
    # 执行文件行数检查和处理逻辑
    for line in json_file_1:
        i += 1
        if i <= processed_lines:
            continue
        if line.strip() == "":
            continue
        item = json.loads(line.strip())

        score = 0
        cnt = 0
        for response in item['response'].keys():
            cnt += 1
            instance = Instance(query=item['prompt'], jailbreak_prompt="", target_responses=[response])
            evaluator._evaluate(instance)
            score += int(instance.eval_results[-1])
        score = score * 1.0 / cnt
        item["score"] = score
        json.dump(item, json_file_2, ensure_ascii=False)
        json_file_2.write('\n')
        # 添加进度条
        if i % 10 == 0:  # 更新进度条频率，根据需要调整
            print(f"Processed lines: {i}")

print("FINISH!")
