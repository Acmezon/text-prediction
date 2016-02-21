#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functions, json, re, string, train, os.path, word_prediction;

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import ttk

## Charge 
unigram_letters_filename = 'training/unigram_letter.json'
bigram_letters_filename = 'training/bigram_letter.json'
unigram_words_filename = 'training/unigram_words.json'
bigram_words_filename = 'training/bigram_words.json'

unigram_letters = None
bigram_letters = None
unigram_words = None
bigram_words = None

code = ''

trained = False

def load_files():
	global trained
	global unigram_letters
	global bigram_letters
	global unigram_words
	global bigram_words

	try:
		with open(unigram_letters_filename) as data_file:
			unigram_letters = json.load(data_file)
		with open(bigram_letters_filename) as data_file:
			bigram_letters = json.load(data_file)
		with open(unigram_words_filename) as data_file:
			unigram_words = json.load(data_file)
		with open(bigram_words_filename) as data_file:
			bigram_words = json.load(data_file)

		trained = True
	except Exception:
		trained = False
		messagebox.showinfo('Entrenamiento', 'El modelo no está entrenado, no predecirá nada hasta que no se vaya a la pestaña entrenamiento y se entrene.')

def getFile(textvar):
	options = { 'multiple': False, 'filetypes': [('Texto', '.txt')] }
	name = filedialog.askopenfilename(**options)

	textvar.set(name)

def train_model(corpus):
	train.train(corpus.get())

	load_files()
	messagebox.showinfo('Entrenamiento', 'Entrenamiento finalizado correctamente.')	

def predict(predicted, number):
	if not trained:
		return

	global code

	predicted_so_far = predicted.get()

	if number == '0':
		code += ' '
		predicted_so_far += ' '
	elif number == '':
		predicted_so_far = word_prediction.run(code, unigram_letters, bigram_letters, unigram_words, bigram_words)
	else:
		code += number
		predicted_so_far = word_prediction.run(code, unigram_letters, bigram_letters, unigram_words, bigram_words)

	predicted.set(predicted_so_far)

def delete(predicted):
	global code

	code = code[:-1]
	predict(predicted, '')

	
root = tk.Tk()
root.title('Predictor de texto')
root.configure(background='white')

style = ttk.Style()

style.theme_create( "bluetabs", parent="alt", settings={
		"TNotebook": {"configure": {"tabmargins": [2, 5, 2, 0] } },
		"TNotebook.Tab": {
			"configure": {"padding": [5, 1], "background": 'white' },
			"map":		 {"background": [("selected", '#cceeff')],
						  "expand": [("selected", [1, 1, 1, 0])] } } } )

style.theme_use("bluetabs")


tabs = ttk.Notebook(root)

prediction = tk.Frame(tabs, background='white')
predicted = tk.StringVar()

entry_predicted = tk.Label(prediction, textvariable=predicted, background='white', foreground='black', font="Calibri 15", borderwidth=0, highlightbackground='white', justify=tk.LEFT, wraplength=270)
entry_predicted.grid(row=0, column=0, ipady=40, columnspan=2)
tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, text='Borrar', command=lambda: delete(predicted), width=15, height=8).grid(row=0, column=2)


tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, text='1', width=15, height=8).grid(row=1, column=0, padx=1, pady=1)
tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '2'), text='a b c\n2', width=15, height=8).grid(row=1, column=1, padx=1, pady=1)
tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '3'), text='d e f\n3', width=15, height=8).grid(row=1, column=2, padx=1, pady=1)

tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '4'), text='g h i\n4', width=15, height=8).grid(row=2, column=0, padx=1, pady=1)
tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '5'), text='j k l\n5', width=15, height=8).grid(row=2, column=1, padx=1, pady=1)
tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '6'), text='m n ñ o\n6', width=15, height=8).grid(row=2, column=2, padx=1, pady=1)

tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '7'), text='p q r s\n7', width=15, height=8).grid(row=3, column=0, padx=1, pady=1)
tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '8'), text='t u v\n8', width=15, height=8).grid(row=3, column=1, padx=1, pady=1)
tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '9'), text='w x y z\n9', width=15, height=8).grid(row=3, column=2, padx=1, pady=1)

tk.Button(prediction, bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0, command=lambda: predict(predicted, '0'), text='Espacio\n0', height=6).grid(row=4, column=0, pady=1, columnspan=3, ipadx=189)

training = tk.Frame(tabs, background='white')

filename = tk.StringVar()

corpus = tk.Entry(training, textvariable=filename, width=30, disabledbackground='white', disabledforeground='black', highlightbackground='black', borderwidth=0)
corpus.config(state=tk.DISABLED)
corpus.grid(row=0, column=0, padx=10, pady=10, ipady=5)

tk.Button(training, text='Corpus (opcional)', command= lambda: getFile(filename), bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0,).grid(row=0, column=1, padx=10, pady=10, ipady=2)

tk.Button(training, text='Entrenar', command= lambda: train_model(corpus), bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0,).grid(row=1, column=0, sticky='w', padx=10)


tabs.add(prediction, text = "Predicción")
tabs.add(training, text = "Entrenamiento")
tabs.pack()

tk.Button(master = root, text='Exit', command = lambda: exit(), bg='white', highlightbackground='black', activebackground='#cceeff', borderwidth=0,).pack(side = tk.LEFT, padx=10, pady=10)

load_files()

tk.mainloop()