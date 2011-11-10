from __future__ import print_function, with_statement
import yaml

def load(source):
    with open(source) as f:
        return map(lambda a: a, yaml.load_all(f))

def ask(questions):
    def _ask(q):
        print(q['q'])
        # XXX: might want to give a nice error about missing id
        # TODO: deal with matches, yesno and options
        return {'a': raw_input(), 'id': q['id']}

    return map(_ask, questions)

