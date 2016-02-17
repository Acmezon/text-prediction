#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functions, json, random;
from train import train;

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
def run(codes, unigram_letters, bigram_letters):
	out = "";
	for code in codes.split():
		out += predict_word(code) + " ";
		
	return out

## Returns most probable word for a single code
def predict_word(code, unigram_letters, bigram_letters):
	new_word = "";
	previous_letter = None;

	for i in range (0, len(code)):
		# for each number of code
		number = int(code[i]);
		if i == 0:
			# if first character of word
			letter = unigram_letter(number, unigram_letters);
		else:
			letter = bigram_letter(previous_letter, number, unigram_letters, bigram_letters)[1];
		previous_letter = letter;
		new_word += letter;
	
	return new_word;


## Returns most probable letter for a dial number.
def unigram_letter(number, unigram_letters):
	candidates = mapping_letters[number];

	max = random.choice(candidates);
	for candidate in candidates:
		if unigram_letters[candidate] > unigram_letters[max]:
			max = candidate;
	return max;

## Returns most probable letter for a dial number with previous letter defined.
def bigram_letter(first_letter, second_number, unigram_letters, bigram_letters):
	key = first_letter + str(second_number);
	if key in bigram_letters:
		candidates = bigram_letters[key];
		max_candidate = random.choice(candidates);
		for tuple in candidates:
			if tuple[1] > max_candidate[1]:
				max_candidate = tuple;
		return max_candidate[0];
	else:
		return first_letter + unigram_letter(second_number, unigram_letters);
	

	