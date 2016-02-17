import codecs
import functions
import json
import os.path
import re
import string
import time
import unicodedata

from collections import Counter
from functions import word_to_number

def train():
	start_time = time.time()
	filename = 'corpus/corpus_sm.txt'

	unigram_letters = 'training/unigram_letter.json'
	bigram_letters = 'training/bigram_letter.json'

	unigram_words = 'training/unigram_words.json'
	bigram_words = 'training/bigram_words.json'


	s = functions.strip_accents(codecs.open(filename, 'r', encoding='utf-8').read().lower());
	words = re.findall(r'\b[a-z]+\b', s)
	bi_words = re.findall(r'(?=([a-z]+\s+[a-z]+))[a-z]+\s+', s)
	
	letters = re.findall(r'[a-z]', s)
	bi_letters = re.findall(r'(?=([a-z][a-z]))[a-z]', s)

	words_count = Counter(words)
	bi_words_count = Counter(bi_words)
	
	letters_count = Counter(letters)
	bi_letters_count = Counter(bi_letters)

	print("Counters took {0} seconds".format(time.time() - start_time))

	print("---------Training begins")

	if(not os.path.isfile(unigram_words)):
		train_unigram_words(words_count, unigram_words);
		print("")
		print("---------Unigram words trained")
	else:
		print("---------Unigram words already trained")

	if(not os.path.isfile(bigram_words)):
		train_bigram_words(bi_words_count, bigram_words);
		print("")
		print("---------Bigram words trained")
	else:
		print("---------Bigram words already trained")

	if(not os.path.isfile(unigram_letters)):
		train_unigram_letters(letters_count, unigram_letters);
		print("---------Unigram letters trained")
	else:
		print("---------Unigram letters already trained")

	if(not os.path.isfile(bigram_letters)):
		train_bigram_letters(bi_letters_count, bigram_letters)
		print("")
		print("---------Bigram letters trained")
	else:
		print("---------Bigram letters already trained")

	print("---------Trainig finished: it tooks {0} seconds".format(time.time() - start_time))

def train_unigram_letters(letters_count, out_filename):
	unigram_letters_trained = dict(letters_count)

	alphabet = list(string.ascii_lowercase);
	for letter in alphabet:
		if letter not in unigram_letters_trained:
			unigram_letters_trained[letter] = 0

	with open(out_filename, 'w') as outfile:
		json.dump(unigram_letters_trained, outfile);

	return

def train_bigram_letters(bi_letters_count, out_filename):
	bigram_letters_trained = {};

	i = 1
	for pair in bi_letters_count.items():
		print(str(i) + "/" + str(len(bi_letters_count.items())), end="\r")
		
		first_letter = pair[0][0]
		second_letter = pair[0][1]
		freq = pair[1]

		number = word_to_number(second_letter)
		code = first_letter + number

		if code in bigram_letters_trained:
			bigram_letters_trained[code].append((pair[0], freq))
		else:
			bigram_letters_trained[code] = [(pair[0], freq)]

		i += 1

	with open(out_filename, 'w') as outfile:
		json.dump(bigram_letters_trained, outfile);

	return

def train_unigram_words(words_count, out_filename):
	unigram_words_trained = {}

	i = 0;
	for pair in words_count.items():
		print(str(i) + "/" + str(len(words_count.items())), end="\r")

		word = pair[0]
		number = functions.word_to_number(word)
		freq = pair[1]

		if number in unigram_words_trained:
			unigram_words_trained[number].append((word, freq))
		else:
			unigram_words_trained[number] = [(word, freq)]
		i += 1

	with open(out_filename, 'w') as fp:
		json.dump(unigram_words_trained, fp)

	return

def train_bigram_words(bi_words_count, out_filename):
	bigram_words_trained = {}

	i = 0
	for pair in bi_words_count.items():
		print(str(i) + "/" + str(len(bi_words_count.items())), end="\r")

		text = (' '.join(pair[0].split())).split()
		first_word = text[0]
		second_word = text[1]
		second_number = word_to_number(second_word)
		freq = pair[1]

		if first_word in bigram_words_trained:
			possibilities = bigram_words_trained[first_word]

			if second_number in possibilities:
				possibilities[second_number].append((second_word, freq))
			else:
				possibilities[second_number] = [(second_word, freq)]
		else:
			bigram_words_trained[first_word] = { second_number: [(second_word, freq)] }

		i += 1

	with open(out_filename, 'w') as fp:
		json.dump(bigram_words_trained, fp)

	return

if __name__ == "__main__":
	train()