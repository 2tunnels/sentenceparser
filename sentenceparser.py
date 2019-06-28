from bs4 import BeautifulSoup
from textblob import TextBlob


def from_text(text: str) -> list:
    blob = TextBlob(text)

    return [str(sentence) for sentence in blob.sentences]


def from_html(html: str) -> list:
    soup = BeautifulSoup(html, 'lxml')

    sentences = []

    for paragraph in soup.find_all('p'):
        sentences.extend(from_text(paragraph.get_text()))

    return sentences
