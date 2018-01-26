#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 17:38:38 2018

@author: huy
"""
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter

#load txt content
strtext = "I have a very nice phone. I drop my phone in the toilet. I find an attorney to sue the toilet, attorney John Due"
#tokenize words and put into 3 dimentional csv or dictionary
tokens = word_tokenize(strtext)
print("tokenizing finished")
# convert to lower case
tokens = [w.lower() for w in tokens]
print("lower case finished")
# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in tokens]
print("removing punctuation finished")
# remove remaining tokens that are not alphabetic
words = [word for word in stripped if word.isalpha()]
print("removing non-alphabetic words finished")
# filter out stop words
stop_words = set(stopwords.words('english'))
words = [w for w in words if not w in stop_words]
print("removing stopwords finished")
#=========== END TEXT PROCESS ===========#

#tokentable = [
#        {"pos":0, "token":"attorney", "occ":1},
#        {"pos":0, "token":"attorney", "occ":1}
#        ]

tokentable = []
#========== main ==========#
print("{}".format("="*30 + " EXTRACT LOG " + "="*30))
print(Counter(words))
#print(tokentable[0])
#print(tokentable[0].get("pos"))
#print(tokentable[0].get("token"))
#print(tokentable[0].get("occ"))



#keyword detect "attorney" "Attorney"
#