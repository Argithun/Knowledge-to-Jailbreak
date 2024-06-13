import torch
import json
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM
import csv

model_path = "/data3/MODELS/vicuna-7b-v1.5"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

original_prompt_list = list()
knowledge_prompt_list = list()
generated_prompt_list = list()
subject_list = list()

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

def generate_answer(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(**inputs,  max_new_tokens=512)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)

def gen_response_for_list(model, prompt_list):
    answers = []
    for prompt in tqdm(prompt_list, desc="Generating responses"):
        answers.append(generate_answer(prompt))
    return answers
    
    
# response_list_1 = gen_response_for_list(model, original_prompt_list)
response_list_2 = gen_response_for_list(model, knowledge_prompt_list)
response_list_3 = gen_response_for_list(model, generated_prompt_list)

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
    
with open('res_vicuna-7b_chem.json', 'w') as json_file:
        json.dump(output, json_file, ensure_ascii=False, indent=4)