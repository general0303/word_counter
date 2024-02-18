import nltk
import codecs
import string


remove_punct_dict = dict((ord(p), None) for p in string.punctuation)

with codecs.open("text.txt", "r", "utf_8_sig") as f:
    text = f.read()
word_tokens = nltk.word_tokenize(text.translate(remove_punct_dict))

print(word_tokens)
