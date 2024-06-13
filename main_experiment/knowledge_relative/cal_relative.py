import json
from rouge_score import rouge_scorer
import matplotlib.pyplot as plt
import numpy as np

scorer = rouge_scorer.RougeScorer(['rouge1'], use_stemmer=True)
# ['rouge1', 'rouge2', 'rougeL']

def convert(sentence):
    sentence=sentence.strip()
    sentence=sentence.replace("<unk>","UNK")
    sentence=sentence.replace("<", "&lt;")
    sentence=sentence.replace(">", "&gt;")
    return sentence

def cal_relative(item1, item2):
    item1 = convert(item1)
    item2 = convert(item2)
    scores = scorer.score(item1, item2)
    rouge_1 = scores['rouge1']
    
    return rouge_1.fmeasure


original_prompt_to_knowledge = {}

with open('../../3_prompt_and_knowledge.json', 'r') as json_file:
    for line in json_file:
        item = json.loads(line)
        original_prompt_to_knowledge[item['prompt']] = item['knowledge'][0]
        
original_relative_list = []
knowledge_relative_list = []
generated_relative_list = []

with open('../all_test.json', 'r') as json_file:
    data = json.load(json_file)
    
for item in data:
    knowledge = original_prompt_to_knowledge[item['original_prompt']]
    original_relative_list.append(cal_relative(knowledge, item['original_prompt']))
    knowledge_relative_list.append(cal_relative(knowledge, item['knowledge_prompt']))
    generated_relative_list.append(cal_relative(knowledge, item['generated_prompt']))
    
def plot_histogram(data, bins=10, range=(0, 1), title='Histogram', xlabel='Value', ylabel='Frequency'):
    plt.figure(figsize=(10, 6))
    plt.hist(data, bins=bins, range=range, edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.savefig(title+'_r1.png')
    
def plot_stacked_histogram(data_list, bins=20, range=(0, 1), title='Stacked Histogram', xlabel='ROUGE-1', ylabel='Frequency', labels=None):
    plt.figure(figsize=(10, 6))
    
    # Compute the histograms
    hist_data = [np.histogram(data, bins=bins, range=range)[0] for data in data_list]
    
    # Stack the histograms
    cumulative_hist_data = np.cumsum(hist_data, axis=0)
    
    # Width of each bin
    bin_width = (range[1] - range[0]) / bins
    bin_edges = np.linspace(range[0], range[1], bins, endpoint=False)
    
    # Plot each histogram in the stack
    i = 0
    colors = ["tab:grey", "tab:orange","tab:purple"]
    for data in data_list:
        color = colors[i]
        if i == 0:
            plt.bar(bin_edges, hist_data[i], width=bin_width, align='edge', label=labels[i] if labels else None, color=color)
        else:
            plt.bar(bin_edges, hist_data[i], width=bin_width, align='edge', bottom=cumulative_hist_data[i-1], label=labels[i] if labels else None, color=color)
        i += 1
        
    # plt.title(title)
    # plt.xlabel(xlabel)
    # plt.ylabel(ylabel)
    # plt.legend()
    # plt.grid(True)
    # plt.savefig(title+'.pdf')
        # Adjust font sizes
    plt.title(title, fontsize=20)
    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontsize=18)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    
    # Move legend to the upper left corner
    plt.legend(loc='upper left', fontsize=18)
    plt.grid(True)
    
    # Save the figure
    plt.savefig(title+'.pdf')

# plot_histogram(original_relative_list, title='Correlation Value between Original_prompt and Knowledge')
# plot_histogram(knowledge_relative_list, title='Correlation Value between Knowledge_prompt and Knowledge')
# plot_histogram(generated_relative_list, title='Correlation Value between Generated_prompt and Knowledge')

plot_stacked_histogram([original_relative_list, knowledge_relative_list, generated_relative_list], 
                         title='ROUGE-1 Score between Prompt and Knowledge',
                         labels=['RE', 'KE', 'Jailbreak-generator'])