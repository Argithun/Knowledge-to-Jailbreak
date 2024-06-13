import os
os.environ["HTTP_PROXY"]="http://127.0.0.1:7898"
os.environ["HTTPS_PROXY"]="http://127.0.0.1:7898"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

from transformers import HfArgumentParser, AutoTokenizer
from tools.inference_models import GenerationArguments, get_inference_model
from tqdm import tqdm
import json
from dataclasses import dataclass, field
import pandas as pd

import wandb
import time

@dataclass
class MyGenerationArguments(GenerationArguments):
    template_path: str = field(default="./templates/zero_shot.json", metadata={"help": "The path to the template file"})
    max_prompt_length: int = field(default=2000, metadata={"help": "The maximum length of the prompt"})
    is_debug: bool = field(default=False, metadata={"help": "Whether to run in debug mode(only 100 sample from each dataset)"})
    model_type: str = field(default="chat", metadata={"help": "The type of model to use for generation"})
    run_name: str = field(default="response_generation", metadata={"help": "The name of the run"})

def generate_response(model, data):
    prompts = [example["prompt"] for example in data]
    # truncate 
    # for i, prompt in enumerate(prompts):
    #     tokenized_prompt = tokenizer(prompt, truncation=False, return_tensors="pt").input_ids[0]
    #     if len(tokenized_prompt) > max_length:
    #         half = int(max_length/2)
    #         prompt = tokenizer.decode(tokenized_prompt[:half], skip_special_tokens=True)+tokenizer.decode(tokenized_prompt[-half:], skip_special_tokens=True)
    #         prompts[i] = prompt
    # print(f"greedy responses for {len(prompts)} prompts")
    # greedy_responses = model.greedy_generate(prompts)
    print(f"sampling responses for {len(prompts)} prompts")
    sampling_responses = model.sampling_generate(prompts)

    return pd.DataFrame({
        "subject": [example["subject"] for example in data], 
        "prompt": prompts, 
        "response": sampling_responses,
    })

def generate_response_light(model, prompt_list):
    prompts = prompt_list
    # truncate 
    # for i, prompt in enumerate(prompts):
    #     tokenized_prompt = tokenizer(prompt, truncation=False, return_tensors="pt").input_ids[0]
    #     if len(tokenized_prompt) > max_length:
    #         half = int(max_length/2)
    #         prompt = tokenizer.decode(tokenized_prompt[:half], skip_special_tokens=True)+tokenizer.decode(tokenized_prompt[-half:], skip_special_tokens=True)
    #         prompts[i] = prompt
    # print(f"greedy responses for {len(prompts)} prompts")
    # greedy_responses = model.greedy_generate(prompts)
    print(f"sampling responses for {len(prompts)} prompts")
    sampling_responses = model.sampling_generate(prompts)

    return sampling_responses

def create_output_dir(run_name):
    output_dir = f"./outputs/{run_name}"
    output_dir += f"_{time.strftime('%Y-%m-%d_%H-%M', time.localtime(time.time()+3600*8))}" # UTC+8
    unqiue_id = 0
    while os.path.exists(output_dir) and os.listdir(output_dir): # if exists and not empty
        log_dir += f"_{unqiue_id}"
        unqiue_id += 1
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")
    return output_dir

def load_template(template_path):
    # log the template file
    prompt_artifact = wandb.Artifact(name="template", type="prompt")
    prompt_artifact.add_file(template_path)
    wandb.log_artifact(prompt_artifact)

    templates = json.load(open(template_path))
    context_template_fn = lambda question, context: '\n'.join(templates['with_context']).format(question=question, context=context)
    no_context_template_fn = lambda question: '\n'.join(templates['without_context']).format(question=question)
    return context_template_fn, no_context_template_fn, templates['context_stop_sign'], templates['question_stop_sign']

def main():
    parser = HfArgumentParser(MyGenerationArguments)
    generation_args = parser.parse_args_into_dataclasses()[0]
    batch_size = generation_args.batch_size

    wandb.init(project="HallucinationDetection", name=generation_args.run_name, config=generation_args)
    print(f"Generation Arguments: {generation_args}")
    
    output_dir = create_output_dir(generation_args.run_name)
    context_template_fn, no_context_template_fn, context_stop_sign, question_stop_sign = load_template(generation_args.template_path)
    
    # we log one example for each dataset to better understand the generated responses
    log_columns = ["id", "prompt", "greedy_response", "ground_truth"]
    generate_example_table = wandb.Table(columns=log_columns)
    wandb.config['output'] = []

    model = get_inference_model(generation_args)
    # ds_names = ["coqa", "nq", "squad", "triviaqa"]
    ds_names = ["waterbench", "nq1500"]

    for ds_name in ds_names:
        if generation_args.is_debug:
            ds_path = f"./data/debug/{ds_name}_sample.json"
            print(f"Debug mode: Using sampled {ds_name} dataset")
        else:
            ds_path = f"./data/processed/{ds_name}.json"
            print(f"Full mode: Using full {ds_name} dataset")
        data = json.load(open(ds_path))
        
        if 'context' in data[0]:
            template_fn = context_template_fn
            model.generation_args.stop_sign = context_stop_sign
        else:
            template_fn = no_context_template_fn
            model.generation_args.stop_sign = question_stop_sign
        model.update_sampling_params()

        print(f"Generating responses for {ds_name} dataset")
        model_name = generation_args.model_name
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        df = generate_response(model, data, template_fn, tokenizer, generation_args.max_prompt_length)
        output_path = os.path.join(output_dir, f"{ds_name}_responses.jsonl")
        df.to_json(output_path, orient="records", lines=True)
        print(f"Responses saved to {output_path}")
        # log last example
        last_row = df.iloc[-1].to_dict()
        generate_example_table.add_data(*[str(last_row[k]) for k in log_columns])
        wandb.config['output'].append(output_path)

    model.delete_model()
    wandb.log({"generated_responses": generate_example_table})
    wandb.finish()
            
if __name__ == "__main__":
    main()