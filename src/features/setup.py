#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 13:08:33 2018

@author: Huy
"""

# nltk packages validate
import nltk

def validateNLTK():
    try:
        nltk_usage = ['tokenizers/punkt', 'corpora/stopwords']
        for i in nltk_usage:
            nltk.data.find(i)
            print('Package validated : ' + nltk.data.find(i))
    except LookupError as e:
        print('Error: '+e)
        nltk.download('popular')
        
        
print(validateNLTK())