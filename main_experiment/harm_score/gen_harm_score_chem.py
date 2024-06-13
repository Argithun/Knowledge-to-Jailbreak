from easyjailbreak.selector.RandomSelector import RandomSelectPolicy
from easyjailbreak.datasets import JailbreakDataset, Instance
from easyjailbreak.seed import SeedTemplate
from easyjailbreak.mutation.generation import Rephrase
from easyjailbreak.models import from_pretrained
from sentence_transformers import SentenceTransformer, util
from easyjailbreak.metrics.Evaluator.Evaluator_ClassificationGetScore import EvaluatorClassificationGetScore
import torch
import json
from tqdm import tqdm

from transformers import HfArgumentParser, AutoTokenizer
from tools.inference_models import GenerationArguments, get_inference_model
from tools.generate_response import MyGenerationArguments, generate_response, generate_response_light

model_1 = from_pretrained('/data2/tsq/WaterBench/data/models/llama-2-7b-chat-hf', 
                        'llama-2', dtype=torch.bfloat16, max_new_tokens=200)
evaluator = EvaluatorClassificationGetScore(model_1)

def evaluate_one_case(prompt, response):
    if response.strip() == "":
        response = "I'm sorry, but I cannot provide assistance."
    instance = Instance(query=prompt, jailbreak_prompt="", target_responses=response)
    evaluator._evaluate(instance)
    return int(instance.eval_results[-1])

def evaluate_harm(file_name):
    with open('../' + file_name, 'r') as file:
        data = json.load(file)
        
    for item in tqdm(data, desc="Processing items", unit="item"):
        # original_score = evaluate_one_case(item['original_prompt'], item['original_prompt_response'])
        knowledge_score = evaluate_one_case(item['knowledge_prompt'], item['knowledge_prompt_response'])
        generated_score = evaluate_one_case(item['generated_prompt'], item['generated_prompt_response'])
        # item['original_score'] = original_score
        item['knowledge_score'] = knowledge_score
        item['generated_score'] = generated_score
        
    with open('score_' + file_name, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

evaluate_harm('res_finance-chat_chem.json')
evaluate_harm('res_gpt-3.5-1106_chem.json')
evaluate_harm('res_gpt-4-1106_chem.json')
evaluate_harm('res_law-chat_chem.json')
evaluate_harm('res_llama-2-7b_chem.json')
evaluate_harm('res_llama-2-13b_chem.json')
evaluate_harm('res_Mistral-7B_chem.json')
evaluate_harm('res_vicuna-7b_chem.json')