# This file will create the functions to use on the training file

# This library will help to cleam the terminal
import os
# This library will help to tokenize and and take the stem of the words
import nltk 
# Maybe you will need to remove the # here and download punk to use nltk
# nltk.download('punk')
# This will help us to remove commoner morphological and inflexional endings from words in English
from nltk.stem.porter import PorterStemmer
# Numpy will help us with zeros method
import numpy as np

stemer = PorterStemmer()

os.system('cls')

def tokenize(sentence):
    # Here we will tokenize the words, break into small pieces
    return nltk.word_tokenize(sentence)


def stem(word):
    # Here we will take the stem of the words
    return stemer.stem(word.lower())


def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0

    return bag
