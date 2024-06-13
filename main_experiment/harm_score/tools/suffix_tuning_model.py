from peft import PeftModelForSequenceClassification, PeftConfig, get_peft_config, PrefixTuningConfig, PrefixEncoder
from peft.utils import _get_batch_size
import torch
from typing import Dict, Any
from transformers.models.mistral import MistralForSequenceClassification
from transformers.models.llama import LlamaForSequenceClassification
from transformers.models.gpt2 import GPT2ForSequenceClassification

class SuffixTuningModelForSequenceClassification(PeftModelForSequenceClassification):
    def __init__(self, model: torch.nn.Module, peft_config: PeftConfig, adapter_name: str = "default") -> None:
        if isinstance(model, MistralForSequenceClassification):
            peft_config.num_attention_heads = model.config.num_key_value_heads
            peft_config.token_dim = model.config.hidden_size // model.config.num_attention_heads * model.config.num_key_value_heads
        super().__init__(model, peft_config, adapter_name)
        self.final_token = torch.nn.Embedding(1, model.config.hidden_size).to(self.device)

    def append_key_values(self, past_key_values, afterwards_key_values):
        if past_key_values is None:
            return afterwards_key_values
        new_past_key_values = []
        for p, a in zip(past_key_values, afterwards_key_values):
            new_key = torch.cat([p[0], a[0].to(p[0].device)], dim=2)
            new_value = torch.cat([p[1], a[1].to(p[1].device)], dim=2)
            new_past_key_values.append((new_key, new_value))
        return tuple(new_past_key_values)

    def forward(
        self,
        input_ids=None,
        attention_mask=None,
        inputs_embeds=None,
        past_key_values=None,
        labels=None,
        output_attentions=None,
        output_hidden_states=None,
        return_dict=None,
        task_ids=None,
        **kwargs,
    ):
        return_dict = return_dict if return_dict is not None else self.config.use_return_dict
        # peft_config = self.active_peft_config
        batch_size = _get_batch_size(input_ids, inputs_embeds)

        # we don't need to expand attention mask
        afterwards_key_values = self.get_prompt(batch_size)
        kwargs.update(
            {
                "input_ids": input_ids,
                "attention_mask": attention_mask,
                "inputs_embeds": inputs_embeds,
                "output_attentions": output_attentions,
                "output_hidden_states": output_hidden_states,
                "return_dict": return_dict,
                "past_key_values": past_key_values,
            }
        )
        # core model forward
        if isinstance(self.base_model, MistralForSequenceClassification) or isinstance(self.base_model, LlamaForSequenceClassification):
            normal_output = self.base_model.model(**kwargs)
        elif isinstance(self.base_model, GPT2ForSequenceClassification):
            normal_output = self.base_model.transformer(**kwargs)
        else:
            raise NotImplementedError(f"Model {self.base_model.__class__} not supported")
        past_key_values = normal_output.past_key_values
        # last_hidden_state_device = normal_output.last_hidden_state.device
        
        # do final token forward
        past_key_values = self.append_key_values(past_key_values, afterwards_key_values)
        kwargs.update({
            "past_key_values": past_key_values,
            'inputs_embeds': self.final_token(torch.zeros(batch_size, 1, dtype=torch.long).to(self.device)),
            'input_ids': None,
            'attention_mask': None,
            # 'labels': labels.to(last_hidden_state_device), # 遇到了一个device问题，还是外面算吧
        })
        final_output = self.base_model(**kwargs)
        logits = final_output.logits
        labels = labels.to(logits.device)
        loss_fct = torch.nn.CrossEntropyLoss()
        final_output['loss'] = loss_fct(logits.view(-1, self.base_model.num_labels), labels.view(-1)) # 神奇，不能用final_output.loss
        return final_output



        
def my_get_peft_config(config_dict: Dict[str, Any]) -> PeftConfig:
    if config_dict["peft_type"] == "SUFFIX_TUNING":
        return PrefixTuningConfig(**config_dict)
    return get_peft_config(config_dict)

if __name__ == "__main__":
    peft_config = my_get_peft_config({
        'peft_type': 'SUFFIX_TUNING',
        "task_type": "CAUSAL_LM",
        "inference_mode": False,
        "num_virtual_tokens": 20,
    })
    from transformers import AutoModelForSequenceClassification, AutoTokenizer
    model = SuffixTuningModelForSequenceClassification(
        model = AutoModelForSequenceClassification.from_pretrained("/data/MODELS/gpt2"),
        peft_config=peft_config,
    )
    model.to(torch.device("cuda:5"))
    sentence = "This is a test sentence"
    tokenizer = AutoTokenizer.from_pretrained("/data3/MODELS/gpt2")
    tokenizer.pad_token_id = tokenizer.eos_token_id
    inputs = tokenizer(sentence, return_tensors="pt", padding=True)
    inputs = {k: v.to("cuda:5") for k, v in inputs.items()}
    outputs = model(**inputs, labels=torch.tensor([1]).to("cuda:5"))
    print(outputs.loss)