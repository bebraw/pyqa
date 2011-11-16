from __future__ import print_function
from functools import partial
from questions import boolean, choice


def ask(questions, answers={}):
    def _fill(i):
        def _f(o):
            o['type'] = o.get('type', 'choice' if o.get('choices') else 'answer') 
            o['id'] = o.get('id') # XXX: warn about missing id?
            o['matches'] = o.get('matches', {})
            o['choices'] = o.get('choices', {})
            
            return o

        return map(_f, i)

    def _input(*answers):
        while True:
            user_input = raw_input()

            if len(user_input) == 0 and answers:
                for a in answers:
                    yield a

            yield user_input

    ret = {}
    def _ask(q):
        qid = q['id']
        qtype = q['type']
        qchoices = q['choices']
        question = q['q']
        answer = None

        if qid in answers:
            answer = str(answers[qid])
            question += ' (' + answer + ')'

        print(question)

        user_input = _input(answer)

        if qtype == 'choice' and answer not in qchoices:
            user_input = _input('Other', answer)

        a = {
            'answer': lambda: user_input.next(),
            'choice': partial(choice, qchoices, user_input),
            'boolean': partial(boolean, user_input),
        }[qtype]()

        ret[qid] = a

    map(_ask, _fill(questions))

    return ret

