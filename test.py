# -*- coding: utf-8 -*-
import json, re, codecs, functions, word_prediction;

def create_set(filename):

	cut_percent = 0;
	text = codecs.open(filename, 'r', encoding='utf-8').read();
	new_len = int(len(text) * cut_percent/100);

	part = text[new_len:]

	sentences = []
	for line in part.splitlines()[1:]:
		parts = line.split(".");
		for x in parts:
			if len(x)>0:
				x = x.strip()
				x = x.replace('á', 'a')
				x = x.replace('ä', 'a')
				x = x.replace('é', 'e')
				x = x.replace('ë', 'e')
				x = x.replace('í', 'i')
				x = x.replace('ï', 'i')
				x = x.replace('ó', 'o')
				x = x.replace('ö', 'o')
				x = x.replace('ú', 'u')
				x = x.replace('ü', 'u')
				x = ''.join(e for e in x if e.isalnum() or e == ' ')
				
				x = re.sub(r'[0-9]+', '', x)

				sentences.append(x.lower());

	with open('corpus/test.json', 'w') as fp:
		json.dump(sentences, fp)

def test():
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

	
	filenames = ['texto_coloquial.txt', 'texto_culto.txt', 'texto_noticia.txt']

	for filename in filenames:
		create_set('corpus/' + filename)

		with open('corpus/test.json', 'r') as fp:
			sentences = json.load(fp)

		words_similarities = []
		sentences_similarities = []

		for sentence in sentences:
			code = functions.sentence_to_numbers(sentence).strip()
			prediction = word_prediction.run(code, unigram_letters, bigram_letters, unigram_words, bigram_words)

			#Sentence similarity
			vector_s_1 = functions.text_to_vector(sentence)
			vector_s_2 = functions.text_to_vector(prediction)
			sentences_similarities.append(functions.get_cosine(vector_s_1, vector_s_2))

			sentence_words = sentence.split()
			prediction_words = prediction.split()
			
			#Word similarity
			for i in range(0, len(sentence_words)):
				vector_w_1 = functions.word_to_vector(sentence_words[i])
				vector_w_2 = functions.word_to_vector(prediction_words[i])
				words_similarities.append(functions.get_cosine(vector_w_1, vector_w_2))

		words_avg = sum(words_similarities) / float(len(words_similarities))
		sentences_avg = sum(sentences_similarities) / float(len(sentences_similarities))

		print("Similaridad media en el {0}:\n\t-Frases: {1:.2f}\n\t-Palabras: {2:.2f}".format(filename.replace('_', ' ').replace('.txt', ''), sentences_avg, words_avg))


if __name__=="__main__":
	test()