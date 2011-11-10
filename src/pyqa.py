from __future__ import print_function, with_statement
import yaml

def load(source):
    with open(source) as f:
        return map(lambda a: a, yaml.load_all(f))

def ask(questions):
    def _fill(i):
        def _f(o):
            o['type'] = o.get('type', 'choice' if o.get('choices') else 'answer') 
            o['id'] = o.get('id') # XXX: warn about missing id?

            return o

        return map(_f, i)

    def _ask(q):
        def _choice():
            map(lambda (i, c): print(str(i) + ': ' + c), enumerate(q['choices']))

            # TODO: make sure input is within proper range
            # TODO: deal with matches
            return raw_input()

        a = {
            'answer': lambda: raw_input(),
            'choice': _choice,
            'yesno': lambda: raw_input().lower() in ('yes', '1', 'true'),
        }[q['type']]()
        
        return {'a': a, 'id': q['id']}

    return map(_ask, _fill(questions))

