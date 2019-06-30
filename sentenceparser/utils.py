import re

import requests
from bs4 import BeautifulSoup
from textblob import TextBlob


def normalize_sentence(sentence: str) -> str:
    """Remove extra spaces from sentence."""

    sentence = sentence.strip()
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


def is_proper_sentence(sentence: str) -> bool:
    if re.match(r'^\w(.*?)[.!?]', sentence):
        return True

    return False


def from_text(text: str) -> list:
    """Parse sentence list from text."""

    blob = TextBlob(text)

    sentences = [str(sentence) for sentence in blob.sentences]
    sentences = [normalize_sentence(sentence) for sentence in sentences]

    return sentences


def from_html(html: str) -> list:
    """Parse sentence list from HTML."""

    soup = BeautifulSoup(html, 'lxml')

    sentences = []

    for paragraph in soup.find_all('p'):
        sentences.extend(from_text(paragraph.get_text()))

    return sentences


def from_url(url: str) -> list:
    """Parse sentence list from URL."""

    r = requests.get(url)
    r.raise_for_status()

    return from_html(r.text)
