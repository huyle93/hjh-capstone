#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 13:37:51 2017

@author: huyle
"""

import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
ssl._create_default_https_context = ssl._create_unverified_context


class Retriever:
    def __init__(self, url, state):
        self.url = url
        self.state = state
    def retriever(self):
        try:
            if self.state.lower() == "vermont":
                html = urlopen(self.url)
                bsObj = BeautifulSoup(html, "html.parser")
                pdf_url = bsObj.findAll("div", {"class": "views-field views-field-field-document"})
                url_list = []
                print("="*10+"STATE OF VERMONT"+"="*10)
                print("Data is pulling from this URL: " + self.url)
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
            print(e)

# uncomment the code below to test this method
            
#test = Retriever('https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F2014&facet_to_date=01%2F01%2F2016', 'vermont')
#print(test.retriever())