import re

from bs4 import BeautifulSoup
from textblob import TextBlob


def normalize_sentence(sentence: str) -> str:
    sentence = sentence.strip()
    sentence = re.sub(r'\s+', ' ', sentence)

    return sentence


def from_text(text: str) -> list:
    blob = TextBlob(text)

    sentences = [str(sentence) for sentence in blob.sentences]
    sentences = [normalize_sentence(sentence) for sentence in sentences]

    return sentences


def from_html(html: str) -> list:
    soup = BeautifulSoup(html, 'lxml')

    sentences = []

    for paragraph in soup.find_all('p'):
        sentences.extend(from_text(paragraph.get_text()))

    return sentences
