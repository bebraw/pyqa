# pyqa -- Configuration generator

pyqa makes it easier to write terminal based tools which ask the user a bunch of questions and then generate some configuration file based on the answers.

## Usage

See /demos for some working examples.

pyqa provides single function, "ask". It expects a set of questions given in a specific format. The following description is in YAML but you are free to use any other markup language as long as the output matches:

    ---
    id: project_name # id to use at the template
    q: Could you please give the project name? # question shown to the user
    ---
    id: license
    q: Please pick a license for your project?
    choices: # if choices field is used, the user will see these as numbered choice
        - BSD
        - GPL
        - MIT
    ---
    id: use_fizzler
    q: Are you sure you want to use fizzler?
    type: boolean -- this will accept either true or false answer and emits True/False

Note that keywords "Yes" and "No" seem to be converted to booleans by YAML. If you need to use those within choices, remember to use explicit form (ie. "Yes" instead of Yes).

After the user has finished answering "ask" will return the results in a format like this:

    {'project_name': 'myproject', 'license': 'BSD', 'use_fizzler': True}

This format happens to be compatible with [pystache](https://github.com/defunkt/pystache) (Python version of [mustache](http://mustache.github.com/)) and no doubt with many other template engines. Just pass that data to your favorite engine, render and output the file somewhere. Voilá!

## License

pyqa is available under MIT license. See LICENSE for more details.

