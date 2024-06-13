import json
from openai import OpenAI

model_names = ["gpt-4", "gpt-4-0613", "gpt-4-1106-preview", "gpt-3.5-turbo", "gpt-3.5-turbo-0613", "gpt-3.5-turbo-1106"]
url = "https://chatapi.onechats.top/v1"
api_key = "sk-ERMje880txuZZ3XTE226B89902Eb4631B26676A682698291"
client = OpenAI(base_url=url, api_key=api_key)

def get_response(prompt):
    response = client.chat.completions.create(
                    model=model_names[2],   # Pick a model
                    temperature=0,
                    messages=[
                        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
                        {"role": "user", "content": prompt}
                    ]
                )
    return response.choices[0].message.content

def get_response_list(prompt_list, file_name):
    had_gen = 0
    try:
        with open(file_name, 'r') as input:
            for line in input:
                had_gen += 1
    except FileNotFoundError:
        # 如果文件不存在，则创建一个空文件
        with open(file_name, 'w') as file:
            pass
        print(f'{file_name} 不存在，已创建空文件。')
    cnt = 0
    with open(file_name, 'a') as output:
        for item in prompt_list:
            if cnt < had_gen:
                cnt += 1
                continue
            save = {}
            save['prompt'] = get_response(item)
            json.dump(save, output, ensure_ascii=False)
            output.write('\n')
            cnt += 1
            print(str(cnt) + '/' + str(len(prompt_list)))


original_prompt_list = list()
knowledge_prompt_list = list()
generated_prompt_list = list()
subject_list = list()

with open('all_test.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    
for item in data:
    original_prompt_list.append(item['original_prompt'])
    knowledge_prompt_list.append(item['knowledge_prompt'])
    generated_prompt_list.append(item['generated_prompt'])
    subject_list.append(item['subject'])
    
get_response_list(original_prompt_list, '1.json')
get_response_list(knowledge_prompt_list, '2.json')
get_response_list(generated_prompt_list, '3.json')

response_list_1 = get_response_list(original_prompt_list)
with open('1.json', 'w') as json_file:
        json.dump(response_list_1, json_file, ensure_ascii=False, indent=4)

response_list_2 = get_response_list(knowledge_prompt_list)
with open('2.json', 'w') as json_file:
        json.dump(response_list_2, json_file, ensure_ascii=False, indent=4)

response_list_3 = get_response_list(generated_prompt_list)
with open('3.json', 'w') as json_file:
        json.dump(response_list_3, json_file, ensure_ascii=False, indent=4)

response_list_1 = list()
response_list_2 = list()
response_list_3 = list()

with open('1.json', 'r', encoding='utf-8') as json_file:
    for line in json_file:
        item = json.loads(line)
        response_list_1.append(item['prompt'])
with open('2.json', 'r', encoding='utf-8') as json_file:
    for line in json_file:
        item = json.loads(line)
        response_list_2.append(item['prompt'])
with open('3.json', 'r', encoding='utf-8') as json_file:
    for line in json_file:
        item = json.loads(line)
        response_list_3.append(item['prompt'])
    
output = list()
for i in range(0, len(subject_list)):
    output.append({
            'original_prompt': original_prompt_list[i],
            'original_prompt_response': response_list_1[i],
            'knowledge_prompt': knowledge_prompt_list[i],
            'knowledge_prompt_response': response_list_2[i],
            'generated_prompt': generated_prompt_list[i],
            'generated_prompt_response': response_list_3[i],
            'subject': subject_list[i],
        })
    
with open('res_gpt-4-1106.json', 'w') as json_file:
        json.dump(output, json_file, ensure_ascii=False, indent=4)