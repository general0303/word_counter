import nltk
import codecs
import string
from pymorphy2 import MorphAnalyzer


remove_punct_dict = dict((ord(p), None) for p in string.punctuation)
morph = MorphAnalyzer()
counter = {"ADJF": 0, "ADJS": 0, "VERB": 0, "INFN": 0, "ADVB": 0}

with codecs.open(input("Введите имя файла\n"), "r", "utf_8_sig") as f:
    text = f.read()
word_tokens = nltk.word_tokenize(text.translate(remove_punct_dict))
for word in word_tokens:
    part_of_speech = morph.parse(word)[0].tag.POS
    if part_of_speech in counter:
        counter[part_of_speech] += 1
print(f"В тексте представлено:\n"
      f"{counter['ADVB']} наречий,\n"
      f"{counter['VERB'] + counter['INFN']} глаголов,\n"
      f"{counter['ADJF'] + counter['ADJS']} прилагательных")
