import re

import dateparser
import nltk
from num2words import num2words

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt", quiet=True)


def normalize_dates(text: str) -> str:
    date_patterns = re.findall(
        r"\b(\d{1,2}[/-]\d{1,2}[/-]\d{2,4}|\d{4}-\d{1,2}-\d{1,2})\b", text
    )
    for date_str in date_patterns:
        parsed_date = dateparser.parse(date_str)
        if parsed_date:
            spoken_date = parsed_date.strftime("%B %-d, %Y")
            text = text.replace(date_str, spoken_date)
    return text


def clean_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
    text = re.sub(r"<[^>]+>", "", text)  # Remove HTML tags
    text = re.sub(
        r"[^\w\s.,!?\'\-]", "", text
    )  # Remove special characters (keep punctuation)
    return text


def normalize_numbers(text: str) -> str:
    def replace_numbers(match):
        number = match.group(0)
        try:
            return num2words(int(number))
        except Exception:
            return number

    return re.sub(r"\b\d+\b", replace_numbers, text)


def split_sentences(text: str) -> list:
    return nltk.sent_tokenize(text)


def preprocess_text(text: str) -> dict:
    date_normalized = normalize_dates(text)
    cleaned = clean_text(date_normalized)
    normalized = normalize_numbers(cleaned)
    sentences = split_sentences(normalized)

    return {
        "original_text": text,
        "cleaned_text": cleaned,
        "normalized_text": normalized,
        "sentences": sentences,
    }
