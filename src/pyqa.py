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
            def in_range(o, i, j):
                try:
                    return i <= int(o) <= j
                except TypeError:
                    return False
                except ValueError:
                    return False

            print('_choice')

            # TODO: deal with matches
            answer = None
            while not in_range(answer, 0, len(q['choices'])):
                map(lambda (i, c): print(str(i) + ': ' + c), enumerate(q['choices']))
                answer = raw_input()

            return answer

        print(q['q'])

        a = {
            'answer': lambda: raw_input(),
            'choice': _choice,
            'yesno': lambda: raw_input().lower() in ('yes', '1', 'true'),
        }[q['type']]()
        
        return {'a': a, 'id': q['id']}

    return map(_ask, _fill(questions))

