import pyqa

# TODO: move elsewhere. this is here just for dev purposes

''' TODOS:
1. parse yaml
2. set up template
3. set up qa ui
4. output filled template (make sure not to override original!)
'''

def main():
    questions = pyqa.load('questions.yaml')
    answers = pyqa.ask(questions)

    print answers

if __name__ == '__main__':
    main()

