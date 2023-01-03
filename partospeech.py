import  nltk
from nltk.corpus import stopwords
from nltk.tokenize import  word_tokenize,sent_tokenize
stop_words=set(stopwords.words("english"))


print(stop_words)

wordList=[]
txt = "Sukanya, Rajib and Naba are my good friends. " \
"Sukanya is getting married next year. " \
"Marriage is a big step in one’s life." \
"It is both exciting and frightening. " \
"But friendship is a sacred bond between people." \
"It is a special kind of love between us. " \
"Many of you must have tried searching for a friend " \
"but never found the right one."

sent=sent_tokenize(txt)
for i in sent:
    wordList=word_tokenize(i)
    wordList=[w for w in wordList if not w in stop_words]
    tag=nltk.pos_tag(wordList)
    print(tag)