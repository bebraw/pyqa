from __future__ import with_statement
import pystache
import yaml
import pyqa


def read(name):
    data = None

    with open(name, 'r') as f:
        data = f.read()

    return data

def write(name, data):
    with open(name, 'w') as f:
        f.write(data)

def load(source):
    with open(source) as f:
        return map(lambda a: a, yaml.load_all(f))

def main():
    template = read('template.moustache')
    questions = load('questions.yaml')
    answers = pyqa.ask(questions)
    data = pystache.render(template, answers)
    write('output.py', data)

if __name__ == '__main__':
    main()

