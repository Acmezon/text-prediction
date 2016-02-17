import codecs
import json
import os.path
import re
import unicodedata
from collections import Counter

filename = 'corpus/corpus_sm.txt';
unigram_letters = 'training/unigram_letter.json';
bigram_letters = 'training/bigram_letter.json'

def train():
	s = functions.strip_accents(codecs.open('corpus/corpus_sm.txt', 'r', encoding='utf-8').read().lower());
	words = re.findall(r'\b[a-z]+\b', s)
	letters = re.findall(r'[a-z]', s)

	words_count = Counter(words);
	letters_count = Counter(letters);

	total_words = sum(words_count.values())

	unigram_words_trained = {}

	for pair in words_count.items():
		word = pair[0]
		number = functions.word_to_number(word)
		freq = pair[1]

		if(number in unigram_words_trained):
			unigram_words_trained[number].append((word, freq))
		else:
			unigram_words_trained[number] = [(word, freq)]

	with open('training/unigram_words.json', 'w') as fp:
		json.dump(unigram_words_trained, fp)

	print("---------Unigram words trained")

	unigram_letters_trained = {};
	bigram_letters_trained = {};

	for letter in letters:
		unigram_letters_trained[letter] = letters_count[letter];

		for letter2 in letters:
			bigram_letters_trained[letter + letter2] = txt.count(letter + letter2);

	with open(unigram_letters, 'w') as outfile:
		json.dump(unigram_letters_trained, outfile);

	with open(bigram_letters, 'w') as outfile:
		json.dump(bigram_letters_trained, outfile);