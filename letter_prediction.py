#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, re, string, os.path;

mapping_letters = {
	2:["a", "b", "c"],
	3:["d", "e", "f"],
	4:["g", "h", "i"],
	5:["j", "k", "l"],
	6:["m", "n", "o"],
	7:["p", "q", "r", "s"],
	8:["t", "u", "v"],
	9:["w", "x", "y", "z"]};

## Runs the letter prediction
def run():
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

	with open(letter_bigrams) as data_file:
		ocurrences = json.load(data_file);

	candidates = mapping_letters[second_number];

	max = candidates[0];
	for candidate in candidates:
		if ocurrences[first_letter+candidate] > ocurrences[first_letter + max]:
			max = candidate;
	return max;