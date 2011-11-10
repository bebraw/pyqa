from __future__ import with_statement
import yaml

def load_file(source):
    with open(source) as f:
        return map(lambda a: a, yaml.load_all(f))

def main():
    pass

if __name__ == '__main__':
    main()

