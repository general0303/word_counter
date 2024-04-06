import nltk
import codecs
import string
from pymorphy2 import MorphAnalyzer


def count(filename):
    nltk.download('punkt')
    remove_punct_dict = dict((ord(p), None) for p in string.punctuation)

    morph = MorphAnalyzer()
    counter = {"ADJF": 0,
               "ADJS": 0,
               "VERB": 0,
               "INFN": 0,
               "ADVB": 0}
    try:
        with codecs.open(filename, "r", "utf_8_sig") as f:
            for text in f:
                word_tokens = nltk.word_tokenize(text.translate(remove_punct_dict))
                for word in word_tokens:
                    part_of_speech = morph.parse(word)[0].tag.POS
                    counter[part_of_speech] += 1 if part_of_speech in counter else 0
    except FileNotFoundError:
        pass
    return {'ADVB': counter['ADVB'], 'VERB': counter['VERB'] + counter['INFN'],
            'ADJ': counter['ADJF'] + counter['ADJS']}


if __name__ == "__main__":
    counter = count(input("Введите имя файла\n"))
    print(f"В тексте представлено:\n"
          f"{counter['ADVB']} наречий,\n"
          f"{counter['VERB']} глаголов,\n"
          f"{counter['ADJ']} прилагательных")
