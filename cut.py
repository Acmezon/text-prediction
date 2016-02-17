import codecs;

cut_percent = 10;
print('Cutted to ' + str(cut_percent) + "%")

text = codecs.open('corpus/corpus_bg.txt', 'r', encoding='utf-8').read();
new_len = int(len(text) * cut_percent/100);
print('New length: ' + str(new_len))

part = text[:new_len]

text_file = open("corpus/corpus_md.txt", "w")
text_file.write(part)
text_file.close()