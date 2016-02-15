from sys import argv;
import string;

def main():
	script, filename = argv;
	txt = open(filename);
	letters = list(string.ascii_lowercase);
	dict = {};

	mapping_letters = {1:["."],
		2:["a", "b", "c"],
		3:["d" "e", "f"],
		4:["g", "h", "i"],
		5:["j", "k", "l"],
		6:["m", "n", "ñ", "o"],
		7:["p", "q", "r", "s"],
		8:["t", "u", "v"],
		9:["w", "x", "y", "z"]};


	query = input('Input word query: ');

	for word in query.split():
		# Conversion to number
		number_query = word_to_number(word);

		new_word = "";
		for i in range (0, number_query):
			number = int(number_query[i]);
			# Obtain out letter for number
			letter = unigram_by_letters(number)[0];
			new_word += letter;

		print (new_word)


		
## Returns sorted array of most probable letters for a dial.
def unigram_by_letters(dial):
	#TODO


## Returns a dial code string for a word.
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

	for i in range (0, len(word)):
		character = word[i];

		if (character in '?!#@$%^&*_~-£()[]{}|'):
			word.replace(character, '');

		if (mapping_number[character]):
			number += str(mapping_number[character]);
		else:
			print('Character ' + character + ' not recognised');

	return number;




	
	






if __name__=='__main__':
	main();