#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:37:51 2017

@author: huyle
"""
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve


from_year = input("from year: ")
to_year = input("to year: ")

vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F"+from_year+"&facet_to_date=01%2F01%2F"+to_year+""

html = urlopen(vermont_site_url)
bsObj = BeautifulSoup(html, "html.parser")
pdf_url = bsObj.findAll("div", {"class": "views-field views-field-field-document"})
count = 0
print("="*10+"STATE OF VERMONT"+"="*10)
print(vermont_site_url)
for link in pdf_url:
    count += 1
    print("="*10, count)
    print(link.find('a').attrs['href'], "\n")
#print(pdf_url.get('href'))
