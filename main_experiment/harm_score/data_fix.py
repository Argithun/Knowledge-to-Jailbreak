import json 

prompt_score = {}

with open('../../2_original_prompt_res_score.json', 'r') as file:
    for line in file:
        if line.strip() == "":
            continue
        try:
            item = json.loads(line)
            prompt_score[item['prompt_in_en']] = item['score']
        except json.decoder.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            continue
        
def fix_score(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    for item in data:
        item['original_score'] = prompt_score[item['original_prompt']]
        
    with open(file_name, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

fix_score('score_res_finance-chat.json')
fix_score('score_res_gpt-3.5-1106.json')
fix_score('score_res_gpt-4-1106.json')
fix_score('score_res_law-chat.json')
fix_score('score_res_llama-2-7b.json')
fix_score('score_res_llama-2-13b.json')
fix_score('score_res_Mistral-7B.json')
fix_score('score_res_vicuna-7b.json')