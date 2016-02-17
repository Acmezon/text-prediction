# -*- coding: utf-8 -*-
import re
import unicodedata

def strip_accents(s):
	return ''.join(c for c in unicodedata.normalize('NFKD', s)
		if unicodedata.category(c) != 'Mn')

# Returns a dial code string for a word.
## Omits special characters
def word_to_number(word): 
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
		"ñ": 6,
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

	word = ''.join(e for e in word if e.isalnum())
	word = re.sub(r'[0-9]', '', word);
	word = word.replace('á', 'a');
	word = word.replace('é', 'e');
	word = word.replace('í', 'i');
	word = word.replace('ó', 'o');
	word = word.replace('ú', 'u');
	word = word.lower();

	for i in range (0, len(word)):
		character = word[i];

		if (character in mapping_number):
			number += str(mapping_number[character]);
		else:
			print('Character ' + character + ' not recognised');

	return number;

def sentence_to_numbers(sentence):
	out = ""
	for word in ' '.join(sentence.split()).split():
		out += word_to_number(word) + " "
	return out