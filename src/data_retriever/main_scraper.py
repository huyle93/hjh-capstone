#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:37:51 2017

@author: huyle
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
import sys
sys.path.insert(0, '../features')
import pol_UNH.py


from_year = input("from year: ")
to_year = input("to year: ")

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
#    print("="*10, count)
    url_list.append(link.find('a').attrs['href'])
#    print(link.find('a').attrs['href'], "\n")
#print(pdf_url.get('href'))

count = 0
for index, i in enumerate(url_list):
    count +=1
    urlretrieve(i, "../../data/raw/download{}.pdf".format(index+1))
print('Total {} downloaded'.format(count))

pol_UNH.convert_pdf_to_txt("../../data/raw")
