from setuptools import setup


setup(
    name='textrank',
    py_modules=['textrank', 'main'],
    version='0.1.0',
    description='TextRank implementation in Python',
    author='Unknown',
    author_email='',
    url='http://github.com/suminb/textrank',
    install_requires=['networkx', 'nltk', 'numpy', 'click'],
    entry_points='''
        [console_scripts]
        textrank=main:cli
    ''',
)
