from transformers import set_seed
from vllm import LLM, SamplingParams
from vllm.model_executor.parallel_utils.parallel_state import destroy_model_parallel
from dataclasses import dataclass, field
from typing import List, Literal
from collections import Counter
from transformers import AutoTokenizer
import gc
import torch

@dataclass
class GenerationArguments:
    # model_name: str = field(default="/data2/tsq/WaterBench/data/models/llama-2-7b-chat-hf", metadata={"help": "The model name or path"})
    # model_name: str = field(default="/data3/MODELS/llama2-hf/llama-2-13b-chat", metadata={"help": "The model name or path"})
    # model_name: str = field(default="/data3/MODELS/vicuna-7b-v1.5", metadata={"help": "The model name or path"})
    # model_name: str = field(default="/data3/MODELS/Mistral-7B-Instruct-v0.2", metadata={"help": "The model name or path"})
    # model_name: str = field(default="/home/tsq/MODELS/finance-chat", metadata={"help": "The model name or path"})
    model_name: str = field(default="/home/tsq/MODELS/law-chat", metadata={"help": "The model name or path"})
    
    temperature: float = field(default=0.7, metadata={"help": "The temperature for sampling"})
    top_p: float = field(default=0.99, metadata={"help": "The nucleus sampling top_p"})
    top_k: int = field(default=50, metadata={"help": "The nucleus sampling top_k"})
    num_return_sequences: int = field(default=20, metadata={"help": "The number of return sequences"})
    seed: int = field(default=1, metadata={"help": "The random seed"})
    max_new_tokens: int = field(default=512, metadata={"help": "The maximum number of new tokens to generate"})
    batch_size: int = field(default=16, metadata={"help": "The batch size for generation"})
    tensor_parallel_size: int = field(default=1, metadata={"help": "The tensor parallel size"})
    stop_sign: str = field(default=None, metadata={"help": "The stop token for generation"})



class vLLMWrapperForCompletionModel:
    def __init__(self, generation_args):
        self.model = LLM(
            model=generation_args.model_name,
            tokenizer=generation_args.model_name,
            tensor_parallel_size=generation_args.tensor_parallel_size,
            gpu_memory_utilization=0.85,
            max_model_len=2048,
            trust_remote_code=True
        )
        self.generation_args = generation_args
        set_seed(self.generation_args.seed)
        self.update_sampling_params()

    def update_sampling_params(self):
        self.sampling_params = SamplingParams(
            temperature=self.generation_args.temperature,
            top_p=self.generation_args.top_p,
            top_k=self.generation_args.top_k,
            n=self.generation_args.num_return_sequences,
            max_tokens=self.generation_args.max_new_tokens,
            stop=self.generation_args.stop_sign
        )
        self.greedy_samp_params = SamplingParams(
            best_of=1, temperature=0.0, top_p=1, top_k=-1, use_beam_search=False, 
            max_tokens=self.generation_args.max_new_tokens,
            stop=self.generation_args.stop_sign
        )
    
    def prepare_prompts(self, prompts):
        if isinstance(prompts, str):
            prompts = [prompts]
        return prompts
    
    def greedy_generate(self, prompts):
        prompts = self.prepare_prompts(prompts)
        greedy_request_output = self.model.generate(prompts, sampling_params=self.greedy_samp_params)
        return [one_request.outputs[0].text for one_request in greedy_request_output]
    
    def sampling_generate(self, prompts) -> List[Counter]:
        prompts = self.prepare_prompts(prompts)
        samp_request_output = self.model.generate(prompts=prompts, sampling_params=self.sampling_params)
        samp_texts = [[cpl.text for cpl in one_request.outputs if cpl.text.strip()] for one_request in samp_request_output]
        samp_texts_counter = [Counter(texts) for texts in samp_texts]
        return samp_texts_counter
    
    def delete_model(self):
        destroy_model_parallel()
        del self.model
        gc.collect()
        torch.cuda.empty_cache()
        torch.distributed.destroy_process_group()


class vLLMWrapperForChatModel(vLLMWrapperForCompletionModel):
    def __init__(self, generation_args):
        super().__init__(generation_args)
        self.chat_template_fn = self.get_chat_template_fn(generation_args.model_name)

    def get_chat_template_fn(self, model_name):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        chat_template_fn = lambda prompts: [
            tokenizer.apply_chat_template([{'role': 'user', 'content': prompt}], tokenize=False, add_generation_prompt=True)
            for prompt in prompts
        ]
        return chat_template_fn
    
    def prepare_prompts(self, prompts):
        prompts = super().prepare_prompts(prompts)
        return self.chat_template_fn(prompts)

def get_inference_model(generation_args: GenerationArguments):
    if generation_args.model_type == "chat":
        model = vLLMWrapperForChatModel(generation_args)
    elif generation_args.model_type == "completion":
        model = vLLMWrapperForCompletionModel(generation_args)
    else:
        raise ValueError(f"Invalid model type: {generation_args.model_type}")
    return model