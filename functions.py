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

	word = re.sub(r'\?!#@\$%\^&\*_~-£()\[]\{}\|\'', '', word)
	word = re.sub(r'[0-9]', '', word)
	word = word.lower()

	for i in range (0, len(word)):
		character = word[i];

		if (character in mapping_number):
			number += str(mapping_number[character]);
		else:
			print('Character ' + character + ' not recognised');

	return number;