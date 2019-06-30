# sentenceparser

Parsing sentences from text, HTML or URL.

## Install

```bash
pip install sentenceparser
```

## Usage

Parse sentences from text file using CLI:

```bash
sentenceparser from-text ~/Documents/text.txt
```

Parse sentences from HTML file using CLI:

```bash
sentenceparser from-html ~/Documents/site.html
```

Parse sentences from URL using CLI:

```bash
sentenceparser from-url 'https://example.com/'
```

Parse sentences from text file using Python API:

```python
import sentenceparser


text = 'Lorem ipsum dolor sit amet consectetur adipisicing elit...'

for sentence in sentenceparser.from_text(text):
    print(sentence)
```

Parse sentences from HTML file using Python API:

```python
import sentenceparser


html = '<p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p><p>...'

for sentence in sentenceparser.from_html(html):
    print(sentence)
```

Parse sentences from URL using Python API:

```python
import sentenceparser


for sentence in sentenceparser.from_url('https://example.com/'):
    print(sentence)
```

## Development

Pull:

```bash
git pull git@github.com:2tunnels/sentenceparser.git
```

Install:

```bash
pipenv install --dev
```

Test:

```bash
pytest
```
