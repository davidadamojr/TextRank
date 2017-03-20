## TextRank
This is a python implementation of TextRank for automatic keyword and sentence extraction (summarization) as done in https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf. However, this implementation uses Levenshtein Distance as the relation between text units.

This implementation carries out automatic keyword and sentence extraction on 10 articles gotten from http://theonion.com

 - 100 word summary
 - Number of keywords extracted is relative to the size of the text (a third of the number of nodes in the graph)
 - Adjacent keywords in the text are concatenated into keyphrases

### Usage
To install the library run the `setup.py` module located in the repository's root directory.  Alternatively, if you have access to pip you may install the library directly from github:

```
pip install git+git://github.com/davidadamojr/TextRank.git
```

Use of the library requires downloading nltk resources.  Use the `textrank initialize` command to fetch the required data.  Once the data has finished downloading you may execute the following commands against the library:

```
textrank extract_summary <filename>
textrank extract_phrases <filename>
```

### Contributing
Install the library as "editable" within a virtual environment.

```
pip install -e .
```


### Dependencies
Dependencies are installed automatically with pip but can be installed serparately.

* Networkx - https://pypi.python.org/pypi/networkx/
* NLTK 3.0 - https://pypi.python.org/pypi/nltk/3.2.2
* Numpy - https://pypi.python.org/pypi/numpy
* Click - https://pypi.python.org/pypi/click


