#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functions, json, re, string, train, os.path;

from tkinter import *
from tkinter import filedialog
from ttk import *

def getFile(textvar):
	options = { 'multiple': False, 'filetypes': [('Texto', '.txt')] }
	name = filedialog.askopenfilename(**options)

	textvar.set(name)

def train_model(parent, corpus):
	trained = train.train(corpus.get())


	
root = Tk()
root.title('Predictor de texto')

tabs = Notebook(root)

prediction = Frame(tabs)
Button(prediction, text='1').grid(row=0, column=0)
Button(prediction, text='2').grid(row=0, column=1)
Button(prediction, text='3').grid(row=0, column=2)

Button(prediction, text='4').grid(row=1, column=0)
Button(prediction, text='5').grid(row=1, column=1)
Button(prediction, text='6').grid(row=1, column=2)

Button(prediction, text='7').grid(row=2, column=0)
Button(prediction, text='8').grid(row=2, column=1)
Button(prediction, text='9').grid(row=2, column=2)

training = Frame(tabs)

filename = StringVar()
corpus = Entry(training, textvariable=filename)
corpus.config(state=DISABLED)
corpus.pack(side=LEFT, padx=10, pady=10)
Button(training, text='Corpus (opcional)', command= lambda: getFile(filename)).pack(side=LEFT, padx=10, pady=10)

Button(training, text='Entrenar', command= lambda: train_model(training, corpus)).pack(side=RIGHT, padx=10, pady=10)


tabs.add(prediction, text = "Predicción")
tabs.add(training, text = "Entrenamiento")
tabs.pack()

Button(master = root, text='Exit', command = lambda: exit()).pack(side = LEFT)
mainloop()