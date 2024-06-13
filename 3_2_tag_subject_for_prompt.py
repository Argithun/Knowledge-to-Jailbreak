import json

prompt_to_subject = {}
with open('./data/0_original_prompt.json', 'r', encoding='utf-8') as file:
    for line in file:
        item = json.loads(line)
        prompt_to_subject[item['prompt_in_en']] = item['subject']

with open('/data1/tsq/FactMark/data/retrieve/JailExpert/output.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
with open('./data/3_prompt_and_knowledge.json', 'a') as json_file:
    for item in data:
        prompt = item['question']
        subject = prompt_to_subject.get(prompt, "unknown")
        knowledge_list = list()
        for knowledge in item['ctxs']:
            knowledge_list.append(knowledge['text'])
        json.dump({'prompt': prompt, 'subject': subject, 'knowledge': knowledge_list}, json_file, ensure_ascii=False)
        json_file.write('\n')
        