This is a python implementation of TextRank for automatic keyword and sentence extraction (summarization) as done in https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf. However, this implementation uses Levenshtein Distance as the relation between text units.

This implementation carries out automatic keyword and sentence extraction on 10 articles gotten from http://theonion.com

 - 100 word summary
 - Number of keywords extracted is relative to the size of the text (a third of the number of nodes in the graph)
 - Adjacent keywords in the text are concatenated into keyphrases

Dependencies
============
Networkx - http://networkx.github.io/download.html
NLTK 3.0 - http://nltk.org/install.html
Numpy - http://sourceforge.net/projects/numpy/files/


