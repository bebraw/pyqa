from __future__ import print_function
from functools import partial
from questions import boolean, choice, match


def ask(questions, answers={}):
    def _fill(i):
        def _f(o):
            o['type'] = o.get('type', 'choice' if o.get('choices') else 'answer') 
            o['id'] = o.get('id') # XXX: warn about missing id?
            o['matches'] = o.get('matches', {})
            o['choices'] = o.get('choices', {})
            
            return o

        return map(_f, i)

    def _input(answer):
        while True:
            user_input = raw_input()

            if len(user_input) == 0 and answer:
                yield answer

            yield user_input

    def union(f, g):
        def _ret():
            return g(f())

        return _ret

    ret = {}
    def _ask(q):
        qid = q['id']
        question = q['q']
        answer = None

        if qid in answers:
            answer = str(answers[qid])
            question += ' (' + answer + ')'

        print(question)

        # TODO: figure out how to deal with choice match and predefined
        # answer! need to redesign that
        user_input = _input(answer)
        a = {
            'answer': lambda: user_input.next(),
            'choice': union(partial(choice, q['choices'], user_input),
                partial(match, q['matches'], user_input)),
            'boolean': partial(boolean, user_input),
        }[q['type']]()

        ret[qid] = a

    map(_ask, _fill(questions))

    return ret

