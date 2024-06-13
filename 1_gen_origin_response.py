from easyjailbreak.selector.RandomSelector import RandomSelectPolicy
from easyjailbreak.datasets import JailbreakDataset, Instance
from easyjailbreak.seed import SeedTemplate
from easyjailbreak.mutation.rule import Translate
from easyjailbreak.models import from_pretrained
from sentence_transformers import SentenceTransformer, util
from easyjailbreak.metrics.Evaluator.Evaluator_ClassificationGetScore import EvaluatorClassificationGetScore
import torch
import json

from transformers import HfArgumentParser, AutoTokenizer
from tools.inference_models import GenerationArguments, get_inference_model
from tools.generate_response import MyGenerationArguments, generate_response, generate_response_light


prompt_list = list()
json_list = list()
with open('./data/0_original_prompt.json', 'r', encoding='utf-8') as file:
    for line in file:
        if line.strip() == "":
            continue
        data = json.loads(line.strip())
        json_list.append(data)
        prompt_list.append(data["prompt_in_en"])

parser = HfArgumentParser(MyGenerationArguments)
generation_args = parser.parse_args_into_dataclasses()[0]
model = get_inference_model(generation_args)


response_list = generate_response_light(model, prompt_list)


with open('./data/1_original_prompt_with_response.json', 'a') as json_file:
    for i in range(len(response_list)):
        json_list[i]["response"] = response_list[i]
        json.dump(json_list[i], json_file, ensure_ascii=False)
        json_file.write('\n')