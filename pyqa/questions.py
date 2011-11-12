def boolean(answers):
    yes = ('yes', '1', 'true')
    no = ('no', '0', 'false')

    answer = None
    while (answer not in yes) and (answer not in no):
        answer = answers.next().strip().lower()

    return answer in yes

