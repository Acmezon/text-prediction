import json, re, codecs, functions, word_prediction;

def create_set():

	cut_percent = 99.99;
	text = codecs.open('corpus/corpus_bg.txt', 'r', encoding='utf-8').read();
	new_len = int(len(text) * cut_percent/100);

	part = text[new_len:]

	chars_to_remove=['(',')','[',']','!','|','@','#','$','%','&','?','¿','¡','^','"','.','+',':',';','º','ª'];

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
				sentences.append(x);

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

	with open('corpus/test.json', 'r') as fp:
		sentences = json.load(fp)

	for sentence in sentences:
		code = functions.sentence_to_numbers(sentence).strip()
		print(word_prediction.run(code, unigram_letters, bigram_letters, unigram_words, bigram_words))


if __name__=="__main__":
	create_set()
	test()