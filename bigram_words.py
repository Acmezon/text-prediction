#-*-coding:utf-8-*-
import codecs
import functions
import json
import math
import os.path
import re
from collections import Counter
from pprint import pprint

def train():
	s = functions.strip_accents(codecs.open('corpus/corpus_sm.txt', 'r', encoding='utf-8').read().lower());
	words = re.findall(r'\b[a-z]+\b', s)

	checked = []
	frequencies = Counter(words)
	trained = {}

	for i in range(0, len(words) - 1):
		print(str(i) + "/" + str(len(words)), end="\r")
		first_word = words[i];
		second_word = words[i+1];

		pair = first_word + " " + second_word
		if not pair in checked:
			checked.append(pair)

			second_number = functions.word_to_number(second_word)

			occurrences = re.findall(r'\b' + re.escape(first_word) + r'\b.{1}\b' + re.escape(second_word) + r'\b', s)
			if first_word in trained:
				possibilities = trained[first_word]

				if second_number in possibilities:
					trained[first_word][second_number].append((second_word, len(occurrences)))
				else:
					trained[first_word][second_number] = [(second_word, len(occurrences))]
			else:
				possibilities = {}
				possibilities[second_number] = [(second_word, len(occurrences))]
				trained[first_word] = possibilities

	with open('training/bigram_words.json', 'w') as fp:
		json.dump(trained, fp)

def predict_word(first_word, second_number):
	if(not os.path.isfile('training/bigram_words.json')):
		train()

def main(text):
	data = {}
	with open('training/bigram_words.json') as training_data:    
		data = json.load(training_data)

	numbers = text.split(" ");

	prediction = []

	first = True
	for number in numbers:
		if first:
			first = False
			#Llamar al unigram de palabra para que resuelva la primera y guardarla en prediction


		first_word = prediction[len(prediction) - 1]
		second_number = number

		possibilities = data[first_word][second_number];

		result = max(possibilities, key=lambda tuple: tuple[1])

		prediction.append(result[0])
		
	res = prediction.join(' ') #mira que esto esté bien

	return res