from sentence_transformers import SentenceTransformer, util
from tqdm import tqdm 
import torch
import json
import os
import csv

from transformers import HfArgumentParser, AutoTokenizer
from tools.inference_models import GenerationArguments, get_inference_model
from tools.generate_response import MyGenerationArguments, generate_response_greedy, generate_response_light

# model = from_pretrained('/data2/tsq/WaterBench/data/models/llama-2-7b-chat-hf', 
#                         'llama-2', dtype=torch.bfloat16, max_new_tokens=200)
parser = HfArgumentParser(MyGenerationArguments)
generation_args = parser.parse_args_into_dataclasses()[0]
model = get_inference_model(generation_args)

original_prompt_list = list()
knowledge_prompt_list = list()
generated_prompt_list = list()
subject_list = list()

# with open('all_test.json', 'r', encoding='utf-8') as file:
#     data = json.load(file)
    
# for item in data:
#     original_prompt_list.append(item['original_prompt'])
#     knowledge_prompt_list.append(item['knowledge_prompt'])
#     generated_prompt_list.append(item['generated_prompt'])
#     subject_list.append(item['subject'])
    
    
file_path = '/home/tsq/pzr_use/code_for_eassy/split_train_test/chem.csv'
with open(file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        original_prompt_list.append(row['original_prompt'])
        knowledge_prompt_list.append(row['knowledge'] + '. ' + row['original_prompt'])
        subject_list.append('化学')  

file_path_1  ='/home/tsq/pzr_use/code_for_eassy/sft/output/meta-llama/Llama-2-7b/seed/0/human_chemistry/generated_0.csv'
with open(file_path_1, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        generated_prompt_list.append(row['generated'])

# def gen_response_for_list(prompt_list):
#     responses_list = generate_response_greedy(model, prompt_list)
#     return responses_list

def gen_response_for_list(model, prompt_list):
    responses = generate_response_light(model, prompt_list)
    output_list = list()
    for i in range(len(responses)):
        cnt = 0
        for response in responses[i].keys():
            cnt += 1
            output_list.append(response)
            if cnt == 1:
                break
    return output_list


# response_list_1 = generate_response_greedy(model, original_prompt_list)
response_list_2 = generate_response_greedy(model, knowledge_prompt_list)
response_list_3 = generate_response_greedy(model, generated_prompt_list)

output = list()
for i in range(0, len(subject_list)):
    output.append({
            # 'original_prompt': original_prompt_list[i],
            # 'original_prompt_response': response_list_1[i],
            'knowledge_prompt': knowledge_prompt_list[i],
            'knowledge_prompt_response': response_list_2[i],
            'generated_prompt': generated_prompt_list[i],
            'generated_prompt_response': response_list_3[i],
            'subject': subject_list[i],
        })
    
with open('res_law-chat_chem.json', 'w') as json_file:
        json.dump(output, json_file, ensure_ascii=False, indent=4)