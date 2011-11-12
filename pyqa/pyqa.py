from __future__ import print_function
from functools import partial
from questions import boolean, choice, match


def ask(questions):
    def _fill(i):
        def _f(o):
            o['type'] = o.get('type', 'choice' if o.get('choices') else 'answer') 
            o['id'] = o.get('id') # XXX: warn about missing id?
            o['matches'] = o.get('matches', {})
            o['choices'] = o.get('choices', {})
            
            return o

        return map(_f, i)

    def _input():
        while True:
            yield raw_input()

    def union(f, g):
        def _ret():
            return g(f())

        return _ret

    ret = {}
    def _ask(q):
        print(q['q'])

        a = {
            'answer': lambda: _input().next(),
            'choice': union(partial(choice, q['choices'], _input()),
                partial(match, q['matches'], _input())),
            'boolean': partial(boolean, _input()),
        }[q['type']]()

        ret[q['id']] = a

    map(_ask, _fill(questions))

    return ret

