#!/usr/bin/env python
'''This demo illustrates how to set up a persistent questionnaire. The main
advantage of this approach is that you have less to fill in case you have
already filled the questionnaire before. In addition it is possible to
share these answers between multiple questionnaires as long as the given
ids match.

In this case I decided to use JSON to store the questions. Other formats
would likely work quite as well.

If you are missing the deps, use "pip install -r requirements.txt".
'''
from __future__ import print_function, with_statement
import json
import pystache
import yaml
import pyqa


def read(name):
    data = None

    try:
        with open(name, 'r') as f:
            data = f.read()
    except IOError:
        pass

    return data

def write(name, data):
    with open(name, 'w') as f:
        f.write(data)

def load(source):
    with open(source) as f:
        return map(lambda a: a, yaml.load_all(f))

def main():
    answers_file = 'answers.json'

    template = read('template.moustache')
    questions = load('questions.yaml')
    original_answers = json.loads(read(answers_file) or '{}')

    answers = pyqa.ask(questions, original_answers)
    write(answers_file, json.dumps(answers))

    data = pystache.render(template, answers)
    write('output.py', data)
    print('inspect output.py for results!')

if __name__ == '__main__':
    main()

