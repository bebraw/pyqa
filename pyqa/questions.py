from __future__ import print_function
from string import lower
from copy import copy


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
    shown_choices = copy(choices)
    shown_choices.append('Other')

    answer = ''
    while (not in_range(answer, 0, len(choices) - 1)) and (answer.lower() not in lower_choices):
        map(lambda (i, c): print(str(i) + ': ' + c), enumerate(shown_choices))
        answer = answers.next().strip() or ''

        if answer == str(len(choices)) or answer.lower() == 'other':
            answer = ''
            while not answer:
                answer = answers.next().strip()
            break

    try:
        return choices[int(answer)]
    except ValueError:
        return answer

