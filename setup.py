#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import pyqa
import subprocess

def pandoc(source, from_format, to_format):
    # http://osiux.com/html-to-restructured-text-in-python-using-pandoc
    # raises OSError if pandoc is not found!
    p = subprocess.Popen(['pandoc', '--from=' + from_format, '--to=' + to_format],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE
        )
    return p.communicate(source)[0]

description = 'pyqa makes it easy to write conversational scripts that generate configuration'
try:
    md = open('README.md').read()

    long_description = pandoc(md, 'markdown', 'rst')
except (IOError, OSError):
    print 'check that you have installed pandoc properly and that README.md exists!'
    long_description = description

setup(name='pyqa',
    version=pyqa.__version__,
    description=description,
    long_description=long_description,
    author=pyqa.__author__,
    author_email='bebraw@gmail.com',
    url='http://github.com/bebraw/pyqa',
    license='MIT',
    keywords=['scripting', 'utility', 'configuration', ],
    packages=['pyqa', ],
    package_dir={'pyqa': 'pyqa', },
    install_requires=[
        'setuptools',
        # -*- Extra requirements -*-
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],
    )

