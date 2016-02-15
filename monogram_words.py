#-*-coding:utf-8-*-
from pprint import pprint
from collections import Counter
import re
import unicodedata
import codecs


def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')

s = codecs.open('corpus/corpus_sm.txt', 'r', encoding='utf-8').read().lower();


"""words = re.findall(r'\b\w+\b', open('corpus/corpus_sm.txt').read().lower())
counter = Counter(words);

pprint(counter.most_common(100));"""

print(strip_accents(s))