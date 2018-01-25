#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 02:14:02 2018

@author: huyle
"""
import nltk
import string
from nltk import ngrams
from ngram import NGram
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
result_gram = []
#nltk.download()
sentence = 'The motion is granted. Hello world, the case is complex. John Due, the plaintiff in the case has hired attorney John Smith for the case. Trial Judges: Jane Hillyard'

# google cloud output, store to detect confident
return_obj = ['John Due', 'John H Smith']

# search attonney key word
def hasAttorney(arg):
    if "attorney" in arg:
        return(True)

def findTrialJudges(arg):
    if "Trial Judges" in arg:
        return(True)

# ngram
def findGram(argtxt,n):
    grams_list = []
    sixgrams = ngrams(argtxt.split(), n)
    for grams in sixgrams:
        grams_list.append(grams)
    return grams_list

# main
print(hasAttorney(sentence))
print(findTrialJudges(sentence))
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
#    print(findAttorney(i))
    #store result
    if hasAttorney(i) == True:
        result_gram.append(i)
    count +=1
#print(count)
#print(result_gram)
lastgram = result_gram[-1]
rebuild_lastgram = ' '.join(lastgram)
#lastgram = ' '.join(i)
#for i in result_gram:
#    last_gram = ' '.join(i)

print(rebuild_lastgram)

# 2 approaches here: 1 is to use service to find PERSON entity, 2 is to use part of speech to remove all none PERSON entity

#remove stopwords#
#cachedStopWords = stopwords.words("english")
#def testFuncNew(arg):
#    arg = ' '.join([word for word in arg.split() if word not in cachedStopWords])
#    return arg
######################
#print(testFuncNew(rebuild_result_gram))


