#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:06:32 2018
Procedure
    1. Scans through the documents in raw/text folder. 
    2. Pick documents those are qualified. 
    3. Perform text cleaning.
Output
    New documents are exported as .txt file into processed folder with the same name.
@author: huyle
"""
from keyword_ import Keyword
import re
import string
import time

#================= Variables ====================
start_time = time.time()
key = "attorney"
filename = "../../data/interim/courtdocbacon.txt"
#==================== Regex =====================
"""
Regexes for bag of words are the output from Word2Vec
"""
attorneyRegexes = ["attorney", "lawyer", "sgn"]
#================================================
f = open(filename, 'rt')
#for line in f:
#    if keyword in line:
#        print(line)
text = f.read().lower()
text1 = text.splitlines()
f.close()
keyword = Keyword(key,text)
print(keyword.hasKeyword())
for line in text1:
    if 'attorney' in line:
#    if keyword.hasKeyword()[0] == True: 
        print(line)

    
# split into words by white space
words = text.split()
# remove punctuation from each word
table = str.maketrans('', '', string.punctuation)
stripped = [w.translate(table) for w in words]
#print(stripped)
#print(Counter(stripped))
print("--- %s seconds ---" % (time.time() - start_time))