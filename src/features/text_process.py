#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:37:58 2017

@author: huyle
"""
import nltk
#nltk.download("popular")
import PyPDF2
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
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
    pdfFileObj = open('../../data/raw/download1.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("extracting data to interim...")
    pages = pdfReader.getNumPages()
    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        text = str(pageObj.extractText())
        text_list.append(text)
    str_text = "".join(text_list)
#================= PROCESS RAW TXT =====================
    print("{}".format("="*30 + " TEXT PROCESS " + "="*30))
    tokens = word_tokenize(str_text)
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
# counting total words
    count_words = len(words)
#    for i in words:
#        if len(word_tokenize(i)) == 1:
#            count += 1
# count duplicate
# export text
    for i in words:
        stripped_text = ''.join(map(str,i))+"\n"
#        print(stripped_text)
        with open('../../data/processed/' + txt_filename, 'ab') as f:
            f.write(stripped_text.encode('utf-8'))
    print("{}".format("="*30 + " EXTRACT LOG " + "="*30))
    print("{}".format("="*12 + " total " + str(count_words) + " of words "))
    print("{}".format("="*12 + " .txt file exported to /processed "))
except Exception as e:
    print("{} \n {} \n".format("="*30 + " EXTRACT LOG " + "="*30,str(e)))
    

#================= NLTK Name Entity Recognition =====================
#def get_continuous_chunks(text):
#     chunked = ne_chunk(pos_tag(word_tokenize(text)))
#     prev = None
#     continuous_chunk = []
#     current_chunk = []
#     for i in chunked:
#             if type(i) == Tree:
#                     current_chunk.append(" ".join([token for token, pos in i.leaves()]))
#             elif current_chunk:
#                     named_entity = " ".join(current_chunk)
#                     if named_entity not in continuous_chunk:
#                             continuous_chunk.append(named_entity)
#                             current_chunk = []
#             else:
#                     continue
#     return continuous_chunk
#print(words)
#print(get_continuous_chunks(str_text))
#================= NLTK Sentiment =====================


