#!/usr/bin/env bash

set -euxo pipefail

echo '🤘 Building...'
python setup.py sdist bdist_wheel

echo '🤘 Checking...'
twine check dist/*

echo '🤘 Publishing...'
twine upload dist/*
