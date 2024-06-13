import json

with open('../data/can_jailbreak_with_knowledge.json', 'r') as file:
    data = json.load(file)
    
simp_list = list()
for item in data:
    simp_list.append({
        'original_prompt': item['prompt'],
        'knowledge': item['knowledge'],
        'prompt': item['prompt_with_knowledge'],
        'mutated_prompt': item['mutated_prompts'][-1],
        'mutated_prompt_score': item['mutated_prompt_malicious_scores'][-1],
        'subject': item['subject']
    })
    
with open('can_jailbreak.json', 'w') as json_file:
        json.dump(simp_list, json_file, ensure_ascii=False, indent=4)