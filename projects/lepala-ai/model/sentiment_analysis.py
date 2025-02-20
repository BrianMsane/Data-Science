"""
Fine tune model for sentiment analysis for langauge in {Swahili, Hausa}
"""

import numpy as np
from sklearn.metrics import f1_score, accuracy_score
from datasets import load_dataset
from typing import Literal
from utils import split_dataset, tokenize_data
from transformers import TrainingArguments, Trainer, AutoTokenizer, AutoModelForCausalLM


def compute_metrics(logits_and_labels):
    logits, labels = logits_and_labels
    prediction = np.argmax(logits, axis=-1)
    return {
        "f1_score": f1_score(labels, prediction, average="weighted"),
        "accuracy": accuracy_score(labels, prediction),
    }


def main(
    dataset_name: str,
    model: AutoModelForCausalLM,
    tokenizer: AutoTokenizer,
    language: Literal["swa", "hau"],
):
    data = load_dataset(dataset_name)
    data = split_dataset(data)
    data = tokenize_data(data)

    training_args = TrainingArguments(
        output_dir="../weights",
        evaluation_strategy="epoch",
        save_strategy="epoch",
        num_train_epochs=3,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=64,
        learning_rate=1e-4,
        warmup_steps=500,
        weight_decay=0.01,
        logging_dir="./logs",
        seed=42,
    )

    trainer = Trainer(
        model=model,
        training_args=training_args,
        train_dataset=data["train"],
        eval_dataset=data["test"],
        compute_metrics=compute_metrics,
        tokenizer=tokenizer,
    )
    trainer.train()
    trainer.evaluate()
