#!/usr/bin/env python
# -*- coding: utf-8 -*-

import letter_prediction, word_prediction, functions, json;
from train import train;

def main():
	## asdasdasd
	number = functions.sentence_to_numbers("tenemos tomates al ajillo con patatas y coresterol");
	print(number)

	train();

	## Charge 
	unigram_letters_filename = 'training/unigram_letter.json'
	bigram_letters_filename = 'training/bigram_letter.json'

	unigram_words_filename = 'training/unigram_words.json'
	bigram_words_filename = 'training/bigram_words.json'

	with open(unigram_letters_filename) as data_file:
		unigram_letters = json.load(data_file)

	with open(bigram_letters_filename) as data_file:
		bigram_letters = json.load(data_file)

	with open(unigram_words_filename) as data_file:
		unigram_words = json.load(data_file)

	with open(bigram_words_filename) as data_file:
		bigram_words = json.load(data_file)




	print(word_prediction.run(number, unigram_letters, bigram_letters, unigram_words, bigram_words));

if __name__=='__main__':
	main();