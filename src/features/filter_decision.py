#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:06:32 2018

@author: huyle
"""
import time
from collections import Counter
start_time = time.time()
from flashtext.keyword import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword = 'Attorney'
filename = "../../data/interim/courtdocbacon.txt"
#strtxt = 'I have a very nice phone. I drop my phone in the toilet. I find an attorney to sue the toilet, attorney John Due'
#with open(filename) as f:
f = open(filename, 'rt')
#for line in f:
#    if keyword in line:
#        print(line)
text = f.read()
f.close()

def hasKeyword(keyword, data):
    keyword_processor.add_keyword(keyword)
    result = keyword_processor.extract_keywords(data)
    if len(result) > 0:
        return True, Counter(result)
    else:
        return "NOPE"
print(hasKeyword(keyword,text))

    
# split into words by white space
words = text.split()
# remove punctuation from each word
import string
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
#print(stripped)
#print(Counter(stripped))
print("--- %s seconds ---" % (time.time() - start_time))