#!/usr/bin/env python

from distutils.core import setup

import textrank


def readme():
    try:
        with open('README.rst') as f:
            return f.read()
    except:
        return '(Could not read from README.rst)'


setup(name='textrank',
      py_modules=['textrank'],
      version=textrank.__version__,
      description='TextRank implementation in Python',
      long_description=readme(),
      author=textrank.__author__,
      author_email=textrank.__email__,
      url='http://github.com/suminb/textrank',
      packages=[],
      )
