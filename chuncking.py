import nltk
sen="The boy is riding in car"
word=nltk.word_tokenize(sen)
print(word)
word_tag=nltk.pos_tag(word)
print(word_tag)
grammer="<NN>:{<DT>?<JJ>*<NN>}"
chunking=nltk.RegexpParser(grammer)
chuncked=chunking.parse(word_tag)
chuncked.draw()