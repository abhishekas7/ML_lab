import nltk
from nltk.util import ngrams
sen="Hello welcome to amaljyothi college of engineering"
word=nltk.word_tokenize(sen)
NGRAMS=ngrams(word,n=3)
for i in NGRAMS: 
    print(i)