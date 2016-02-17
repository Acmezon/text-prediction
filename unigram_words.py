#-*-coding:utf-8-*-
import codecs
import functions
import json
import os.path
import re
import unicodedata
from collections import Counter
from pprint import pprint

def train():
	s = functions.strip_accents(codecs.open('corpus/corpus_sm.txt', 'r', encoding='utf-8').read().lower());
	words = re.findall(r'\b[a-z]+\b', s)
	counter = Counter(words);

	total = sum(counter.values())

	trained = {}

	for pair in counter.items():
		word = pair[0]
		number = functions.word_to_number(word)
		freq = pair[1] / total

		if(number in trained):
			trained[number].append((word, freq))
		else:
			trained[number] = [(word, freq)]

	with open('training/unigram_words.json', 'w') as fp:
		json.dump(trained, fp)



def predict_word(number):
	if(not os.path.isfile('training/unigram_words.json')):
		train()

	data = {}
	with open('training/unigram_words.json') as training_data:    
		data = json.load(training_data)

	if not number in data:
		return None

	possibilities = data[number];

	result = max(possibilities, key=lambda tuple: tuple[1])

	return result[0]

def run(text):
	prediction = ""

	for word in words:
		number = functions.word_to_number(word)

		prediction += predict_word(number) + " "

	print(prediction)