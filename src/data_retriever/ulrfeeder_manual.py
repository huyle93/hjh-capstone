#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:50:03 2017

@author: Huy
"""

import ssl
from bs4 import BeautifulSoup
from urllib.request import urlopen, urlretrieve
ssl._create_default_https_context = ssl._create_unverified_context

class URLGenerator(object):
    def urlGenerator(self):
        
        """[summary]
            what it does?
                Generating all the URLs where the scraper will use to pull data from
            input
                from_year: int
                to_year: int
                option: str 
                    // division name or all
                state: str
                files: str 
                    // int(str) or "max"
            ouput
                list of url str
                ["url1", "url2",...]
        """
        
        # VERMONT #
        baseurl = 'https://www.vermontjudiciary.org'
        path = '/opinions-decisions'
        # from date
        param1 = 'facet_from_date=01/01'
        # to date
        param2 = 'facet_to_date=01/01/'
        # division
        param3 = 'f%5B0%5D=court_division_opinions_library%3A'
        # search by text
        param4 = 'search_api_fulltext='
        # page
        param5 = 'page='
        # generate list of URL
        listURL = []
        
        # list of divisions
        vt_court_division = {"civil": "1", "supreme court": "7", "environmental": "3", "family": "4", "criminal": "2"}
        # inputs
        from_year = 2000
        to_year = 2017
        endPages = 75 #0-74
        startPages = 0
        # make change to pull data from different division by changing division name below to any of the division in vt_court_vivision dict
        division = vt_court_division["environmental"]
        # url generating
        for i in range(startPages, endPages):
            build_url = baseurl + path + '?' + param1 + str(from_year) + "&" + param2 + str(to_year) + "&" + param3 + division + param4 + "&" + param5 + str(i) + ""
            # append url to listUrl
            listURL.append(build_url)
            i += 1
        
        # return full list of URLs
        return listURL


# uncomment the code below to test this method
#test = URLGenerator()
#print(test.urlGenerator())
