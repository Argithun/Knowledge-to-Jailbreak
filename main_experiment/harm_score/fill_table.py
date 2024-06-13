import json

def fill_one_blank(file_name, domain_list):
    print(file_name + " : " + str(domain_list))
    with open(file_name, 'r') as input:
        data = json.load(input)
    
    ori_sum = 0
    know_sum = 0
    gen_sum = 0
    num = 0
    
    for item in data:
        if item['subject'] in domain_list:
            num += 1
            ori_sum += item['original_score']
            know_sum += item['knowledge_score']
            gen_sum += item['generated_score']
    
    # print('ori:')
    print(str(round(ori_sum/num, 2)) + ' & ' + str(round(know_sum/num, 2)) + ' & ' + str(round(gen_sum/num, 2)))
    # # print('know:')
    # print(know_sum/num)
    # # print('gen:')
    # print(gen_sum/num)
    
# fill_one_blank('score_res_finance-chat.json', ['政治经济学'])

# ['公安学', '社会学', '政治经济学', 'unknown', '网络安全', '法学', '心理学']

files = ['score_res_finance-chat.json', 'score_res_gpt-3.5-1106.json', 'score_res_gpt-4-1106.json', 'score_res_law-chat.json', 
         'score_res_llama-2-7b.json', 'score_res_llama-2-13b.json', 'score_res_Mistral-7B.json', 'score_res_vicuna-7b.json']

for name in files:
    # fill_one_blank(name, ['公安学'])
    # fill_one_blank(name, ['法学'])
    # fill_one_blank(name, ['政治经济学'])
    # fill_one_blank(name, ['公安学', '社会学', '政治经济学', 'unknown', '网络安全', '法学', '心理学'])
    fill_one_blank(name, ['管理学'])
    fill_one_blank(name, ['计算机科学'])
    fill_one_blank(name, ['地理学'])
    fill_one_blank(name, ['化学', '物理学', '药学', '地理学', '计算机科学', '管理学'])