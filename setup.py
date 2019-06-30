from pathlib import Path

from setuptools import setup

here = Path(__file__).parent

with open(here / 'README.md', mode='r', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='sentenceparser',
    version='0.0.1',
    description='Parsing sentences from text, HTML or URL.',
    long_description=readme,
    long_description_content_type='text/markdown',
    url='https://github.com/2tunnels/sentenceparser',
    author='Vlad Dm',
    author_email='2tunnels@gmail.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['sentenceparser'],
    include_package_data=True,
    install_requires=[
        'textblob>=0.15.3,<1.0',
        'beautifulsoup4>=4.7.1,<5.0',
        'lxml>=4.3.4,<5.0',
        'requests>=2.22.0,<3.0',
        'click>=7.0,<8.0',
    ],
    entry_points={
        'console_scripts': [
            'sentenceparser=sentenceparser.__main__:main',
        ]
    },
)
