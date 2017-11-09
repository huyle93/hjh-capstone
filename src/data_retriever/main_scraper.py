#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:37:51 2017

@author: huyle
"""
#import pol_UNH.py
import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import sys
#from PyPDF2 import PdfFileReader
import PyPDF2
from PyPDF2 import PdfFileReader
#sys.path.insert(0, '../feature/pol_UNH.py')
#from pol_UNH import converter


ssl._create_default_https_context = ssl._create_unverified_context
#from_year = input("from year: ")
#to_year = input("to year: ")

vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F"+from_year+"&facet_to_date=01%2F01%2F"+to_year+""

html = urlopen(vermont_site_url)
bsObj = BeautifulSoup(html, "html.parser")

pdf_url = bsObj.findAll("div", {"class": "views-field views-field-field-document"})
url_list = []
print("="*10+"STATE OF VERMONT"+"="*10)
print("Data is pulling from this URL: " + vermont_site_url)
print("="*10+"DONE"+"="*10)
print("loading...")
for link in pdf_url:
    url_list.append(link.find('a').attrs['href'])
count = 0
#for index, i in enumerate(url_list):
#    count +=1
#    urlretrieve(i, "../../data/raw/download{}.pdf".format(index+1))
print('Total {} downloaded'.format(count))

#converter.convert_pdf_to_txt("../../data/raw")

mylist = []


pdfFileObj = open('../../data/raw/download1.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pages = pdfReader.getNumPages()
for i in range(pages):
    count_page = 0
    pageObj = pdfReader.getPage(i)
    text = str(pageObj.extractText())
#    print(text)
#    print("="*30+str(count)+"="*30)
    
    i +=1
    count +=1
    with open('../../data/interim/download1.txt', 'a') as f:
        f.write(text)
#    mylist.append(text)
#print(mylist)
#pageObj.extractText()

#print(text)

#with open('../../data/interim/download1.txt', 'w') as f:
#    f.write(text)

#inputPdf = PdfFileReader(open('../../data/raw/download1.pdf', "rb"))
#docInfo = inputPdf.getDocumentInfo()
#print(docInfo.title)
