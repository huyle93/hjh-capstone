#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:37:51 2017

@author: huyle
"""

import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import PyPDF2
from retrieve_doc_name import Retriever
ssl._create_default_https_context = ssl._create_unverified_context

#================= User Interface ====================
while True:
    try:
        from_year = int(input("from year: "))
        to_year = int(input("to year: "))
        option = str(input("Please enter a specfic division or all for all: "))
        if len(str(from_year)) != 4:
            print("Please enter year in 4 digits format")
        elif len(str(to_year)) != 4:
            print("Please enter year in 4 digits format")
        else:
            break
    except ValueError:
        print("Please enter number")


#================= Data Source ====================    
urlRetriever = Retriever(from_year, to_year, option)
vermont_site_url = urlRetriever.retriever()

#================= Retrieve Data ====================
try:
    html = urlopen(vermont_site_url)
    bsObj = BeautifulSoup(html, "html.parser")
    pdf_url = bsObj.findAll("div", {"class": "views-field views-field-field-document"})
    url_list = []
    print("="*10+"STATE OF VERMONT"+"="*10)
    print("Data is pulling from this URL: " + vermont_site_url)
    print("="*10+"DONE"+"="*10)
    print("retrieving data...")
    
    for link in pdf_url:
        url_list.append(link.find('a').attrs['href'])
    count = 0
    for index, i in enumerate(url_list):
        count +=1
        urlretrieve(i, "../../data/raw/download{}.pdf".format(index+1))
        
    print('Total {} downloaded'.format(count))
except Exception as e:
    print("{} \n {} \n".format("="*30 + " RETRIEVE LOG " + "="*30,str(e)))
    



#================= Extract PDF =====================
try:
    pdfFileObj = open('../../data/raw/download1.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    print("extracting data to interim...")
    pages = pdfReader.getNumPages()
    for i in range(pages):
        pageObj = pdfReader.getPage(i)
        text = str(pageObj.extractText())
        with open('../../data/interim/download1.txt', 'ab') as f:
            f.write(text.encode('utf-8'))
    print("txt data in interim")
except Exception as e:
    print("{} \n {} \n".format("="*30 + " EXTRACT LOG " + "="*30,str(e)))

