import json
import csv

knowledge_to_mes = {}

with open('../split_train_test/can_jailbreak.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
for item in data:
    knowledge_to_mes[item['knowledge']] = item

generated_prompts = '../sft/output/meta-llama/Llama-2-7b/seed/0/jailbreak_patcher/generated_0.csv'

output = list()
with open(generated_prompts, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)

    # 遍历每一行
    for row in reader:
        # 访问 input 和 generated 字段
        input_value = row['input']
        generated_value = row['generated']
        output.append({
            'original_prompt': knowledge_to_mes[input_value]['original_prompt'],
            'knowledge_prompt': knowledge_to_mes[input_value]['prompt'],
            'generated_prompt': generated_value,
            'subject': knowledge_to_mes[input_value]['subject'],
        })
        
with open('all_test.json', 'w') as json_file:
        json.dump(output, json_file, ensure_ascii=False, indent=4)