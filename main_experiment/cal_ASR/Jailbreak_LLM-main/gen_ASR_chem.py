import json


models = ['law-chat', 'finance-chat', 'llama-2-7b', 'llama-2-13b', 'vicuna-7b', 'Mistral-7B', 'gpt-3.5-1106', 'gpt-4-1106']
domains = ["['化学']"]
ptypes = ['knowledge_prompt', 'generated_prompt']

for model in models:
    num = 0
    for domain in domains:
        print(model+',', end="")
        for ptype in ptypes:
            with open(f"./merged_eval_results/default-only/{model}_{ptype}_{domain}_summary_chem.json", 'r') as file:
                data = json.load(file)
                print(str(data['break_by_all']) + '.0,', end="")
        num += 1
        if num == 4:
            print("\n>>>    ", end="")
    print()