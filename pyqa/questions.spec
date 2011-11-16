def values(*args):
    for arg in args:
        yield arg

def boolval(arg):
    return questions.boolean(values(arg))

accepts boolean
    valid = ('yes', 'Yes', 'YES', '1', 'true', 'True')

    for a in valid:
        boolval(a) == True

rejects boolean
    invalid = ('no', 'No', 'NO', '0', 'false', 'False')

    for a in invalid:
        boolval(a) == False

asks boolean multiple times
    questions.boolean(values('foo', 'bar', 'yes')) == True

accepts choice
    questions.choice(['foo', 'bar', 'baz'], values('0')) == 'foo'

accepts choice by name
    questions.choice(['foo', 'bar', 'baz'], values('foo')) == 'foo'

accepts choice by name with upper
    questions.choice(['foo', 'bar', 'baz'], values('Foo')) == 'Foo'

asks choice multiple times
    questions.choice(['foo', 'bar', 'baz'], values('zob', '3', '2')) == 'baz'

accepts other choice
    questions.choice(['foo', 'bar', 'baz'], values('3', 'booboo')) == 'booboo'

accepts other choice by name
    questions.choice(['foo', 'bar', 'baz'], values('other', 'booboo')) == 'booboo'

accepts other choice by name with upper
    questions.choice(['foo', 'bar', 'baz'], values('oTher', 'booboo')) == 'booboo'

