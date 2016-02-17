#-*-coding:utf-8-*-
from train import train;
import letter_prediction, json;

unigram_words = 'training/unigram_words.json';
bigram_words = 'training/bigram_words.json';

## Runs the word prediction proccess for a large number code
def run(codes, unigram_letters, bigram_letters, unigram_words, bigram_words):

	codes = codes.split();
	prediction = []

	for i in range(0, len(codes)):
		number = codes[i];

		if number != "":
			if i==0:
				# if first
				# Call unigram of words:
				prediction.append(unigram_word(number, unigram_letters, bigram_letters, unigram_words));
			else:
				# get previous words in predictions
				previous_word = prediction[i-1]
				prediction.append(bigram_word(previous_word, number, unigram_letters, bigram_letters, unigram_words, bigram_words)[1])

	# conversion to string
	res =  " ".join([str(x) for x in prediction])
	return res

## Returns the most probable word given the dial code
def unigram_word(number, unigram_letters, bigram_letters, unigram_words):

	if not number in unigram_words:
		# if number not registered
		# return letter prediction for word
		return letter_prediction.predict_word(number, unigram_letters, bigram_letters)
	else:
		possibilities = unigram_words[number];
		# return word with max tuple value
		result = max(possibilities, key=lambda tuple: tuple[1])
		return result[0]

## Returns array with the most probable combination of words given the previous word and the next dial code
def bigram_word(previous_word, second_number, unigram_letters, bigram_letters, unigram_words, bigram_words):
	
	if not previous_word in bigram_words:
		# previous word not registered
		# return unigram for second word
		return [previous_word, unigram_word(second_number, unigram_letters, bigram_letters, unigram_words)]
	else:
		possibilities = bigram_words[previous_word];
		if not second_number in possibilities:
			# combination not registered
			# return unigram for second word
			return [previous_word, unigram_word(second_number, unigram_letters, bigram_letters, unigram_words)]
		else:
			possibilities = possibilities[second_number];
			result = max(possibilities, key=lambda tuple: tuple[1])
			return [previous_word, result[0]]