from __future__ import print_function

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

    answer = None
    while not in_range(answer, 0, len(choices) - 1):
        map(lambda (i, c): print(str(i) + ': ' + c), enumerate(choices))
        answer = answers.next()

    return choices[int(answer)]

def match(matches, choice, answer):
    match = matches.get(choice)

    if match:
        print(match)

        return answer()

