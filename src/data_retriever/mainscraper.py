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


class Retriever(object):
    def __init__(self, url, state):
        self.url = url
        self.state = state
    def retriever(self):
        try:
            if self.state.lower() == "vermont":
                count = 0
                for e in self.url:
                    html = urlopen(e)
                    bsObj = BeautifulSoup(html, "html.parser")
                    pdf_url = bsObj.findAll("div", {"class": "views-field views-field-field-document"})

                    # validate if page has pdf
                    if len(pdf_url) != 0:
                        print("="*10+"STATE OF VERMONT"+"="*10)
                        print("Data is pulling from this URL: " + e)
                        print("="*10+"DONE"+"="*10)
                        print("retrieving data...")
                        
                        # build list of pdf url
                        url_list = []
                        for link in pdf_url:
                            url_list.append(link.find('a').attrs['href'])

                        # loop through href link of pdf
                        for i in (url_list):
                            count +=1
                            urlretrieve(i, "../../data/raw/75/download{}.pdf".format(str(count)))
                            
                        print('Total {} downloaded'.format(count))
        except Exception as e:
            print(e)

# uncomment the code below to test this method
            
#test = Retriever(['https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F2014&facet_to_date=01%2F01%2F2016'], 'vermont')
#print(test.retriever())