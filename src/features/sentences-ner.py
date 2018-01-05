#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:09:56 2018

@author: huyle
"""

import nltk
import sys
import PyPDF2
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk import sent_tokenize
# ****** pipeline *******
# - Extract PDF to txt
# - Process raw txt
# -- convert to lower case
# -- tokenize words
# -- remove punctuation from each word
# -- remove tokens that are not alphabetic
# -- filter stopwords
# - NER
# - JSON dump
# ***********************
#variables
txt_filename = 'download1.txt'
count = 0
text_list = []
#helping defitions
def getTotalWords(s):
    return len(word_tokenize(s))
    
#================= Extract PDF TO TXT ===============================
try:
    pdfFileObj = open('../../data/raw/download2.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("extracting data to interim...")
    pages = pdfReader.getNumPages()
    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        text = str(pageObj.extractText())
        text_list.append(text)
    str_text = "".join(text_list)
#================= PROCESS RAW TXT =====================
    sentences = sent_tokenize(str_text)
except Exception as e:
    print("{} \n {} \n".format("="*30 + " EXTRACT LOG " + "="*30,str(e)))
    

#================= NLTK Name Entity Recognition =====================
def get_continuous_chunks(text):
     chunked = ne_chunk(pos_tag(word_tokenize(text)))
     prev = None
     continuous_chunk = []
     current_chunk = []
     for i in chunked:
             if type(i) == Tree:
                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
             elif current_chunk:
                     named_entity = " ".join(current_chunk)
                     if named_entity not in continuous_chunk:
                             continuous_chunk.append(named_entity)
                             current_chunk = []
             else:
                     continue
     return continuous_chunk
for i in sentences:
    result = get_continuous_chunks(i)
    if result == []:
        pass
    else:
        print(result)
#================= NLTK Sentiment =====================
