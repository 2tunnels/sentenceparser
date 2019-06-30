from pathlib import Path

from sentenceparser.utils import normalize_sentence, from_text, from_html

fixture_path = Path(__file__).parent / 'fixtures'


class TestNormalizeSentence:
    def test(self):
        sentence = 'Et dolor vel quis quos voluptas nesciunt\n    porro ipsa esse quia quae!'
        assert normalize_sentence(sentence) == 'Et dolor vel quis quos voluptas nesciunt porro ipsa esse quia quae!'


class TestFromText:
    def test_one_sentence(self):
        text = ('To be useful, a program usually needs to communicate with the outside world by obtaining input data '
                'from the user and displaying result data back to the user.')
        assert from_text(text) == [text]

        text = ('Ohisalo ei selkeästikään ole vielä ehtinyt perehtyä riittävällä tavalla hallitusohjelman turvapaikka- '
                'ja pakolaispolitiikkaan.')
        assert from_text(text) == [text]

    def test_multiple_sentences(self):
        text = ('Input may come directly from the user via the keyboard, or from some external source like a file or '
                'database. Output can be displayed directly to the console or IDE, to the screen via a Graphical User '
                'Interface (GUI), or again to an external source.')
        assert from_text(text) == [
            ('Input may come directly from the user via the keyboard, or from some external source like a file or '
             'database.'),
            ('Output can be displayed directly to the console or IDE, to the screen via a Graphical User Interface '
             '(GUI), or again to an external source.'),
        ]

        text = ('Ohisalo ei selkeästikään ole vielä ehtinyt perehtyä riittävällä tavalla hallitusohjelman turvapaikka- '
                'ja pakolaispolitiikkaan. Ei sieltä ole mitään linjanmuutosta tulossa, Kurvinen sanoo.')
        assert from_text(text) == [
            ('Ohisalo ei selkeästikään ole vielä ehtinyt perehtyä riittävällä tavalla hallitusohjelman turvapaikka- '
             'ja pakolaispolitiikkaan.'),
            'Ei sieltä ole mitään linjanmuutosta tulossa, Kurvinen sanoo.',
        ]


class TestFromHtml:
    def test_one_sentence(self):
        with open(fixture_path / 'one_sentence.html', mode='r', encoding='utf-8') as f:
            html = f.read()

        assert from_html(html) == ['Lorem ipsum dolor sit, amet consectetur adipisicing elit.']

    def test_multiple_sentences(self):
        with open(fixture_path / 'multiple_sentences.html', mode='r', encoding='utf-8') as f:
            html = f.read()

        assert from_html(html) == [
            'Lorem ipsum dolor sit, amet consectetur adipisicing elit.',
            'Assumenda, magni.',
            ('Et dolor vel quis quos voluptas nesciunt porro ipsa esse quia quae tempore aliquid magni delectus, '
             'perferendis possimus, labore veritatis!'),
        ]

    def test_multiple_paragraphs(self):
        with open(fixture_path / 'multiple_paragraphs.html', mode='r', encoding='utf-8') as f:
            html = f.read()

        assert from_html(html) == [
            'Lorem ipsum dolor sit, amet consectetur adipisicing elit.',
            'Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
            'Example site.'
        ]
