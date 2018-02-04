#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 02:14:02 2018

@author: huyle
"""
# validate nltk data installed


import string
from nltk import ngrams
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from cloudPlatform_request_ import *
result_gram = []

sentence = 'The motion is granted. Hello world, the case is complex. John Due, the plaintiff in the case has hired attorney John H. Smith for the case. Trial Judge: Jane Hillyard.'

############## SEARCH KEYWORD  ################
def hasAttorney(arg):
    if "attorney" in arg:
        return(True)

def findTrialJudges(arg):
    if "Judge" in arg:
        return(True)

############## GET LINES HAVE KEYWORD  ################

############## NGRAMS  ################
def findGram(argtxt,n):
    grams_list = []
    sixgrams = ngrams(argtxt.split(), n)
    for grams in sixgrams:
        grams_list.append(grams)
    return grams_list

############## TEXT PROCESS  ################
def cleanSentence(sentence):
    tokens = word_tokenize(sentence)
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in tokens]
    stripped = list(filter(None, stripped))
    rebuild_sentence = ' '.join(stripped)
    return rebuild_sentence


############## MAIN ################
print("has attorney: "+ str(hasAttorney(sentence)))
print("has judge: "+ str(findTrialJudges(sentence)))
findGram_output = findGram(cleanSentence(sentence),11)
count=0
for i in findGram_output:
#    print(findAttorney(i))
    #store result
    if hasAttorney(i) == True:
        result_gram.append(i)
    count +=1
lastgram = result_gram[-1]
rebuild_lastgram = ' '.join(lastgram)
#print(rebuild_lastgram)

# 2 approaches here: 1 is to use service to find PERSON entity, 2 is to use part of speech to remove all none PERSON entity

#returnFromAPI = entity_sentiment_text(rebuild_lastgram)
#print(returnFromAPI)

#remove stopwords#
#cachedStopWords = stopwords.words("english")
#def testFuncNew(arg):
#    arg = ' '.join([word for word in arg.split() if word not in cachedStopWords])
#    return arg
######################
#print(testFuncNew(rebuild_result_gram))


