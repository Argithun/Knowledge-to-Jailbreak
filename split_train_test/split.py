import json
import random

def split_and_save(data_list, name):
    random.shuffle(data_list)
    split_point = int(len(data_list) * 0.8)
    
    train_set = data_list[:split_point]
    test_set = data_list[split_point:]
    
    with open(f'{name}_train.json', 'w') as train_file:
        json.dump(train_set, train_file, ensure_ascii=False, indent=4)
    
    with open(f'{name}_test.json', 'w') as test_file:
        json.dump(test_set, test_file, ensure_ascii=False, indent=4)

sociology_set = list()
unknown_set = list()
psychology_set = list()
police_set = list()
economics_set = list()
cybersecurity_set = list()
law_set = list()
others_set = list()

with open('can_jailbreak.json', 'r') as file:
    data = json.load(file)

for item in data:
    if item['subject'] == '社会学':
        sociology_set.append(item)
    elif item['subject'] == 'unknown':
        unknown_set.append(item)
    elif item['subject'] == '心理学':
        psychology_set.append(item)
    elif item['subject'] == '公安学':
        police_set.append(item)
    elif item['subject'] == '政治经济学':
        economics_set.append(item)
    elif item['subject'] == '网络安全':
        cybersecurity_set.append(item)
    elif item['subject'] == '法学':
        law_set.append(item)
    else:
        others_set.append(item)
        
split_and_save(sociology_set, 'sociology')
split_and_save(unknown_set, 'unknown')
split_and_save(psychology_set, 'psychology')
split_and_save(police_set, 'police')
split_and_save(economics_set, 'economics')
split_and_save(cybersecurity_set, 'cybersecurity')
split_and_save(law_set, 'law')
with open(f'others_test.json', 'w') as test_file:
        json.dump(list(others_set), test_file, ensure_ascii=False, indent=4)