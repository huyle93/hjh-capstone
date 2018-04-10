#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 17:15:36 2018

@author: Huy
"""
from helpers import getDirectorySize, printArt
# from urlfeeder import URLGenerator
from mainscraper import Retriever
from pdftxtconverter import Converter
from ulrfeeder_manual import URLGenerator
import time

start_time = time.time()
#================= User Interface ====================
while True:
    try:
        state = (input("state: "))
        # from_year = int(input("from year: "))
        # to_year = int(input("to year: "))
        # option = str(input("Please enter a specfic division or all for all: "))
        # if len(str(from_year)) != 4:
        #     print("Please enter year in 4 digits format")
        # elif len(str(to_year)) != 4:
        #     print("Please enter year in 4 digits format")
        # else:
        break
    except ValueError:
        print("Please enter number")

#================= URLGenerator ====================
# input args
# output list of url
try:
    # VM_urlgenerator = URLGenerator(from_year, to_year, option, state)
    VM_urlgenerator = URLGenerator()
    VM_url = VM_urlgenerator.urlGenerator() #list
except Exception as e:
    print("{} \n {} \n".format("="*30 + " RETRIEVE LOG " + "="*30,str(e)))
#================= Retriever ====================
# input list of url
# output downloading data
try:
    VM_retriever = Retriever(VM_url, state)
#    VM_retriever.retriever()
    print(''' LOADING...
‎0███████████████████99%
 ''')
except Exception as e:
    print("{} \n {} \n".format("="*30 + " RETRIEVE LOG " + "="*30,str(e)))

#================= PDF to TXT =====================
try:
    pdfDir = "../../data/raw/75/"
    txtDir = "../../data/interim/75/"
    VM_converter = Converter(pdfDir,txtDir)
    VM_converter.convertMultiple()
    printArt('DONE!')
except Exception as e:
    print("{} \n {} \n".format("="*30 + " EXTRACT LOG " + "="*30,str(e)))
    
#================= Helpers =====================
#pdfDir = "../../data/raw/75/"
print('Total PDF files size in MB: ' + str(getDirectorySize(pdfDir)))
# print('Total Text files size in MB: ' + str(getDirectorySize(txtDir)))
print("--- %s seconds ---" % (time.time() - start_time))