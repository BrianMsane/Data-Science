from datasets import Dataset
import string
import re
from transformers import AutoTokenizer


def load_tokenizer(checkpoint: str):
    """Load the tokenizer specific to the model"""
    return AutoTokenizer.from_pretrained(checkpoint)


def split_dataset(dataset: Dataset, test_size: float = 0.2):
    return dataset["train"].train_test_split(test_size=test_size, seed=42, shuffle=True)


class TextPreprocessor:
    """Cleaning Sentences"""

    def __init__(self, lower: bool = False, emoji: bool = True) -> None:
        self.lower = lower
        self.emoji = emoji

    def clean_text(self, text: str) -> str:
        """Clean the given text by applying necessary methods"""
        try:
            text = self.remove_mentions(text)
            if self.lower:
                text = text.lower()
            text = self.remove_extra_spaces(text)
            text = self.remove_links(text)
            if self.emoji:
                text = self.remove_emojis(text)
            text = self.remove_emoticons(text)
            text = self.remove_tags(text)
            text = self.remove_unicode_character(text)
            text = self.remove_punctuation_marks(text)
            text = self.remove_numbers(text)
            if self.correct:
                text = self.correct_spelling(text)
            return text
        except Exception as e:
            raise e

    def remove_punctuation_marks(self, text: str) -> str:
        return text.translate(str.maketrans("", "", string.punctuation))

    def remove_numbers(self, text: str) -> str:
        return re.sub(r"\d", "", text)

    def remove_extra_spaces(self, text: str) -> str:
        return " ".join(text.split())

    def remove_emojis(self, text: str) -> str:
        return text.encode("ascii", "ignore").decode("ascii")

    def remove_emoticons(self, text: str) -> str:
        emoticon_pattern = r"[:;=][\-\^]?[D\)\]\(\]/\\OpP]"
        return re.sub(emoticon_pattern, "", text)

    def remove_tags(self, text: str) -> str:
        pattern = re.compile(r"<.*?>")
        cleaned_text = re.sub(pattern, "", text)
        return cleaned_text

    def remove_links(self, text: str) -> str:
        url_pattern = re.compile(r"https?://\S+|www\.\S+")
        text = url_pattern.sub("", text)
        return text

    def remove_unicode_character(self, text: str) -> str:
        return re.sub(r"[^\x00-\x7F]+", "", text)

    def stem_words(self, text: str) -> str:
        stem = [self.stemmer.stem(word) for word in text.split()]
        return " ".join(stem)

    def remove_mentions(self, text: str) -> str:
        text = re.sub(r"RT @\w+: ", "", text)
        text = re.sub(r"@\w+", "", text)
        return text
