#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv;
import json, re, string, os.path;

filename = 'corpus/corpus_sm.txt';
letter_monograms = 'training/monogram_letter.json';
letter_bigrams = 'training/bigram_letter.json'

def main():
	train();
	
	query = input('Input word query: ');

	out = "";
	for word in query.split():
		# Conversion to number
		number_query = word_to_number(word);

		new_word = "";
		last_letter = None;
		for i in range (0, len(number_query)):
			number = int(number_query[i]);
			# Obtain out letter for number
			if i == 0:
				# first character of word
				letter = predict_letter(number);
			else:
				letter = predict_letters(last_letter, number);
			last_letter = letter;
			new_word += letter;
		out += new_word + " "
	print(out)


## Save letter ocurrences in JSON format
def train():
	txt = open(filename).read();
	letters = list(string.ascii_lowercase);
	ocurrences = {};
	bigrams = {};

	monogram_learned = os.path.exists(letter_monograms);
	bigram_learned = os.path.exists(letter_bigrams);

	if not monogram_learned or not bigram_learned:
		for letter in letters:
			if not monogram_learned:
				ocurrences[letter] = txt.count(letter);

			if not bigram_learned:
				for letter2 in letters:
					bigrams[letter + letter2] = txt.count(letter + letter2);

	if not monogram_learned:
		with open(letter_monograms, 'w') as outfile:
			json.dump(ocurrences, outfile);

	if not bigram_learned:
		with open(letter_bigrams, 'w') as outfile:
			json.dump(bigrams, outfile);
		
## Returns most probable letter for a dial number.
def predict_letter(dial):

	mapping_letters = {
		2:["a", "b", "c"],
		3:["d", "e", "f"],
		4:["g", "h", "i"],
		5:["j", "k", "l"],
		6:["m", "n", "o"],
		7:["p", "q", "r", "s"],
		8:["t", "u", "v"],
		9:["w", "x", "y", "z"]};

	with open(letter_monograms) as data_file:
		ocurrences = json.load(data_file);

	candidates = mapping_letters[dial];

	max = candidates[0];
	for candidate in candidates:
		if ocurrences[candidate] > ocurrences[max]:
			max = candidate;
	return max;

## Returns most probable letter for a dial number with previous dial.
def predict_letters(first_letter, second_number):
	mapping_letters = {
		2:["a", "b", "c"],
		3:["d", "e", "f"],
		4:["g", "h", "i"],
		5:["j", "k", "l"],
		6:["m", "n", "o"],
		7:["p", "q", "r", "s"],
		8:["t", "u", "v"],
		9:["w", "x", "y", "z"]};

	with open(letter_bigrams) as data_file:
		ocurrences = json.load(data_file);

	candidates = mapping_letters[second_number];

	max = candidates[0];
	for candidate in candidates:
		if ocurrences[first_letter+candidate] > ocurrences[first_letter + max]:
			max = candidate;
	return max;

## Returns a dial code string for a word.
## Omits special characters
def word_to_number(word):
	word.replace('.,?!#@$%^&*_~-£()[]{}|', '');
	word.replace('á', 'a')
	word.replace('é', 'e')
	word.replace('í', 'i')
	word.replace('ó', 'o')
	word.replace('ú', 'u')
	number = "";
	mapping_number = {
		".": 1,
		"a": 2,
		"b": 2,
		"c": 2,
		"d": 3,
		"e": 3,
		"f": 3,
		"g": 4,
		"h": 4,
		"i": 4,
		"j": 5,
		"k": 5,
		"l": 5,
		"m": 6,
		"n": 6,
		"o": 6,
		"p": 7,
		"q": 7,
		"r": 7,
		"s": 7,
		"t": 8,
		"u": 8,
		"v": 8,
		"w": 9,
		"x": 9,
		"y": 9,
		"z": 9};


	for i in range (0, len(word)):
		character = word[i];
		
		if (character in mapping_number.keys()):
			number += str(mapping_number[character]);
		else:
			print('Character ' + character + ' not recognised');

	return number;


if __name__=='__main__':
	main();