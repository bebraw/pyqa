#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import pyqa

setup(name='pyqa',
    version=pyqa.__version__,
    description='pyqa makes it easy to write conversational scripts that generate configuration',
    long_description=open('README.md').read(),
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

