#-*-coding:utf-8-*-
import codecs
import functions
import json
import math
import os.path
import re
from collections import Counter
from itertools import combinations
from pprint import pprint

def train():
	s = functions.strip_accents(codecs.open('corpus/corpus_sm.txt', 'r', encoding='utf-8').read().lower());
	words = re.findall(r'\b[a-z]+\b', s)

	checked = []
	frequencies = Counter(words)
	trained = {}

	for i in range(0, len(words)):
		print("")
		for j in range(i, len(words)):
			print(str(j + len(words) * i) + "/" + str(len(words) * len(words)), end="\r")

			first_word = words[i]
			second_word = words[j]

			pair = first_word + " " + second_word
			if(not pair in checked):
				checked.append(pair)

				occurrences = re.findall(r'\b' + re.escape(first_word) + r'\b.{1}\b' + re.escape(second_word) + r'\b', s)
				if len(occurrences) > 0:
					pair = functions.word_to_number(first_word) + " " + functions.word_to_number(second_word)

					if pair in trained:
						trained[pair].append((second_word, len(occurrences) / frequencies[first_word]))
					else:
						trained[pair] = [(second_word, len(occurrences) / frequencies[first_word])]

			

	with open('training/bigram_words.json', 'w') as fp:
		json.dump(trained, fp)

def predict_word(first_word, second_number):
	if(not os.path.isfile('training/bigram_words.json')):
		train()

def main(text):
	"""data = {}
	with open('training/monogram_words.json') as training_data:    
		data = json.load(training_data)

	words = text.split(" ");

	prediction = ""

	for word in words:
		number = word_to_number(word)

		possibilities = data[number];

		result = max(possibilities, key=lambda tuple: tuple[1])

		prediction += result[0] + " "

	print(prediction)"""

if __name__ == '__main__':
	predict_word("a", "123")