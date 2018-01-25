#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 02:14:02 2018

@author: huyle
"""
import nltk
import string
from nltk import ngrams
from nltk.tokenize import word_tokenize

#nltk.download()
sentence = 'The motion is granted. Hello world, the case is complex. John Due, the plaintiff in the case has hired attorney John Smith for the case.'

# google cloud output, store to detect confident
return_obj = ['John Due', 'John Smith']

# search attonney key word
def findAttorney(arg):
    if "attorney" in arg:
        return(True)


# ngram
def findGram(argtxt,n):
    grams_list = []
    sixgrams = ngrams(argtxt.split(), n)
    for grams in sixgrams:
        grams_list.append(grams)
    return grams_list

# main
print(findAttorney(sentence))
tokens = word_tokenize(sentence)
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
stripped = list(filter(None, stripped))
rebuild_sentence = ' '.join(stripped)
#print(rebuild_sentence)
findGram_output = findGram(rebuild_sentence,4)
#count grams
count=0
for i in findGram_output:
    count +=1
    print(i)
print(count)


