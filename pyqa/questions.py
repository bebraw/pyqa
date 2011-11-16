from __future__ import print_function
from string import lower


def boolean(answers):
    yes = ('yes', '1', 'true')
    no = ('no', '0', 'false')

    answer = None
    while (answer not in yes) and (answer not in no):
        answer = answers.next().strip().lower()

    return answer in yes

def choice(choices, answers):
    def in_range(o, i, j):
        try:
            return i <= int(o) <= j
        except (TypeError, ValueError):
            return False
    lower_choices = map(lower, choices)

    answer = ''
    while (not in_range(answer, 0, len(choices) - 1)) and (answer.lower() not in lower_choices):
        map(lambda (i, c): print(str(i) + ': ' + c), enumerate(choices))
        answer = answers.next() or ''

    try:
        return choices[int(answer)]
    except ValueError:
        return answer

def match(matches, answer, choice):
    match = matches.get(choice)

    if match:
        print(match)

        return answer.next()
    else:
        values = matches.values()

        if choice in values:
            print(matches.keys()[values.index(choice)])

            return answer.next()

    return choice

