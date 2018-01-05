#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 02:32:13 2018

@author: huyle
"""

#from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = '/path/to/standford/jars'
os.environ['STANFORD_MODELS'] = '/path/to/standford/jars'

parser = stanford.StanfordParser(model_path="/location/of/the/englishPCFG.ser.gz")
sentences = parser.raw_parse_sents(("Hello, My name is Melroy.", "What is your name?"))
print(sentences)

# GUI
for line in sentences:
    for sentence in line:
        sentence.draw()