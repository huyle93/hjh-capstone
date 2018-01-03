#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 13:37:58 2017

@author: huyle
"""
import PyPDF2
#================= Extract PDF =====================
try:
    pdfFileObj = open('../../data/raw/download1-test.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("extracting data to interim...")
    pages = pdfReader.getNumPages()
    print("="*40)
#    for i in range(1):
    pageObj = pdfReader.getPage(1)
    text = str(pageObj.extractText())
    print(text)
#        with open('../../data/interim/download1.txt', 'ab') as f:
#            f.write(text.encode('utf-8'))
#    print("txt data in interim")
except Exception as e:
    print("{} \n {} \n".format("="*30 + " EXTRACT LOG " + "="*30,str(e)))
    
#================= Process Text File =====================

#================= NLTK Name Entity Recognition =====================

#================= NLTK Sentiment =====================