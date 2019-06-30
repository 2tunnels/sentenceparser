import click

import sentenceparser


@click.group()
def cli():
    pass


@click.command()
@click.argument('path', type=click.Path(exists=True))
def from_text(path):
    with open(path, mode='r', encoding='utf-8') as f:
        text = f.read()

    for sentence in sentenceparser.from_text(text):
        click.echo(sentence)


@click.command()
@click.argument('path', type=click.Path(exists=True))
def from_html(path):
    with open(path, mode='r', encoding='utf-8') as f:
        html = f.read()

    for sentence in sentenceparser.from_html(html):
        click.echo(sentence)


@click.command()
@click.argument('url')
def from_url(url: str):
    for sentence in sentenceparser.from_url(url):
        click.echo(sentence)


cli.add_command(from_text)
cli.add_command(from_html)
cli.add_command(from_url)

if __name__ == '__main__':
    cli()
