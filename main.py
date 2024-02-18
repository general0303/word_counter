import nltk
import codecs
import string
from pymorphy2 import MorphAnalyzer


remove_punct_dict = dict((ord(p), None) for p in string.punctuation)
morph = MorphAnalyzer()

with codecs.open("text.txt", "r", "utf_8_sig") as f:
    text = f.read()
word_tokens = nltk.word_tokenize(text.translate(remove_punct_dict))
for word in word_tokens:
    print(word, morph.parse(word)[0].tag.POS)

print(word_tokens)
