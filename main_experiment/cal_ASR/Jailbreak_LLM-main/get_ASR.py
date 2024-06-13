import json


models = ['law-chat', 'finance-chat', 'llama-2-7b', 'llama-2-13b', 'vicuna-7b', 'Mistral-7B', 'gpt-3.5-1106', 'gpt-4-1106']
domains = ["['公安学']", 
           "['法学']",
           "['政治经济学']",
           "['公安学', '社会学', '政治经济学', 'unknown', '网络安全', '法学', '心理学']",
           "['管理学']",
           "['计算机科学']",
           "['地理学']",
           "['化学', '物理学', '药学', '地理学', '计算机科学', '管理学']"]
ptypes = ['original_prompt', 'knowledge_prompt', 'generated_prompt']

for model in models:
    num = 0
    for domain in domains:
        for ptype in ptypes:
            with open(f"./merged_eval_results/default-only/{model}_{ptype}_{domain}_summary.json", 'r') as file:
                data = json.load(file)
                print(str(data['break_by_all']) + '.0 & ', end="")
        num += 1
        if num == 4:
            print("\n>>>    ", end="")
    print()