#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import pyqa

description = 'pyqa makes it easy to write conversational scripts that generate configuration'
try:
    from pypandoc import convert

    long_description = convert('README.md', 'rst')
except (ImportError, IOError, OSError):
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

