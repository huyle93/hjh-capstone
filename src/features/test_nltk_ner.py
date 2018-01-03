#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:37:58 2017

@author: huyle
"""
import sys
import PyPDF2
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
txt_filename = 'download1.txt'
#================= Extract PDF =====================
try:
    pdfFileObj = open('../../data/raw/download2.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("extracting data to interim...")
    pages = pdfReader.getNumPages()
    print("="*40)
    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        text = str(pageObj.extractText())
#        print(text)
#================= Process Text Pipeline =====================
        tokens = word_tokenize(text)
        # convert to lower case
        tokens = [w.lower() for w in tokens]
        # remove punctuation from each word
        table = str.maketrans('', '', string.punctuation)
        stripped = [w.translate(table) for w in tokens]
        # remove remaining tokens that are not alphabetic
        words = [word for word in stripped if word.isalpha()]
        # filter out stop words
        stop_words = set(stopwords.words('english'))
        words = [w for w in words if not w in stop_words]
#        print(words)
        for i in words:
            stripped_text = ''.join(map(str,i))+"\n"
#            print(stripped_text)
            with open('../../data/interim/' + txt_filename, 'ab') as f:
                f.write(stripped_text.encode('utf-8'))
#                f.write(i.encode('utf-8'))

    print("txt data in interim")
except Exception as e:
    print("{} \n {} \n".format("="*30 + " EXTRACT LOG " + "="*30,str(e)))
    

#================= NLTK Name Entity Recognition =====================

#================= NLTK Sentiment =====================