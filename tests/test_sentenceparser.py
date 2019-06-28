from sentenceparser import from_text, from_html


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
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit.</p>
</body>
</html>"""
        assert from_html(html) == ['Lorem ipsum dolor sit, amet consectetur adipisicing elit.']

    def test_multiple_sentences(self):
        html = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Assumenda, magni. Et dolor vel quis quos voluptas nesciunt porro ipsa esse quia quae tempore aliquid magni delectus, perferendis possimus, labore veritatis!</p>
</body>
</html>"""
        assert from_html(html) == [
            'Lorem ipsum dolor sit, amet consectetur adipisicing elit.',
            'Assumenda, magni.',
            ('Et dolor vel quis quos voluptas nesciunt porro ipsa esse quia quae tempore aliquid magni delectus, '
             'perferendis possimus, labore veritatis!'),
        ]
