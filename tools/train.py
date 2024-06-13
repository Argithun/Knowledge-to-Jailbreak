from transformers import Trainer, TrainingArguments, AutoModelForSequenceClassification, AutoTokenizer, DataCollatorWithPadding, HfArgumentParser, EarlyStoppingCallback
from datasets import Dataset, load_from_disk
import json
from suffix_tuning_model import SuffixTuningModelForSequenceClassification, my_get_peft_config
from dataclasses import dataclass, field

import logging 
logging.basicConfig(level=logging.ERROR)

def prepare_dataset(tokenizer):
    try:
        dataset = load_from_disk("data/processed_train/internal_states_lama_trex_train")
        print("loaded dataset from disk")
        loaded_from_disk = True
    except Exception as e:
        print(f"failed to load dataset from disk: {e}")
        loaded_from_disk = False
    if not loaded_from_disk:
        internal_states_path = "data/processed_train/internal_states_train.json"
        with open(internal_states_path, "r") as f:
            data = json.load(f)["data"]
        lama_trex_path = "data/processed_train/lama_trex_train.json"
        with open(lama_trex_path, "r") as f:
            data.extend(json.load(f)["data"])
        dataset = Dataset.from_list(data)
        # split the dataset
        dataset = dataset.train_test_split(test_size=0.2, seed=0)
        save_path = "data/processed_train/internal_states_lama_trex_train"
        dataset.save_to_disk(save_path)
        print(f"saved dataset to {save_path}")

    # pretokenize
    def tokenize_function(examples):
        return tokenizer(examples["statement"])
    dataset = dataset.map(tokenize_function, batched=True, desc=f"pre-tokenize using {tokenizer.__class__}")
    return dataset

def compute_metrics(p):
    predictions = p.predictions.argmax(axis=1)
    return {"accuracy": (predictions == p.label_ids).mean()}

@dataclass
class ModelArguments:
    model_name_or_path: str = field(
        default="/data/MODELS/gpt2",
        metadata={"help": "The model checkpoint for weights initialization."},
    )
    num_virtual_tokens: int = field(
        default=5,
        metadata={"help": "The number of virtual tokens."},
    )

if __name__ == "__main__":
    parser = HfArgumentParser((ModelArguments, TrainingArguments))
    model_args, training_args = parser.parse_args_into_dataclasses()

    tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path)
    tokenizer.pad_token_id = tokenizer.eos_token_id
    tokenizer.pad_token = tokenizer.eos_token
    tokenizer.padding_side = "left"

    dataset = prepare_dataset(tokenizer)
    
    peft_config = my_get_peft_config({
        'peft_type': 'SUFFIX_TUNING',
        "task_type": "SEQUENCE_CLASSIFICATION",
        "inference_mode": False,
        "num_virtual_tokens": model_args.num_virtual_tokens,
    })
    model = SuffixTuningModelForSequenceClassification(
        model = AutoModelForSequenceClassification.from_pretrained(model_args.model_name_or_path, device_map="auto"),
        peft_config=peft_config,
    )
    model.config.pad_token_id = tokenizer.eos_token_id

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset["train"],
        eval_dataset=dataset["test"],
        data_collator=data_collator,
        compute_metrics=compute_metrics,
        callbacks=[EarlyStoppingCallback(early_stopping_patience=3)],
    )
    trainer.train()

