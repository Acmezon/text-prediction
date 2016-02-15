#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, re, string, os.path;

filename = 'corpus/corpus_sm.txt';
letter_monograms = 'training/monogram_letter.json';
letter_bigrams = 'training/bigram_letter.json'


if __name__=='__main__':
	main();