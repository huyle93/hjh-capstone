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
    def __init__(self, from_year, to_year, option, state, files):
        self.from_year = from_year
        self.to_year = to_year
        self.option = option
        self.state = state
        self.files = files
        
    def urlGenerator(self):
        
        """[summary]
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

        # state is Vermont
        if self.state.lower() == "vermont" or self.state.lower() == "vm":
            # all division
            if self.option.lower() == "all":
                # if input is max
                if self.files == 'max':
                    pages = 0
                    build_url = baseurl + path + '?' + param1 + str(self.from_year) + "&" + param2 + str(self.to_year) + "&" + param4 + "&" + param5 + str(pages) + ""
                    # append url to listUrl
                    listURL.append(build_url)
                    pages += 1
                # if input is a number
                else:
                    try:
                        self.files = int(self.files)
                    except ValueError:
                        pass  # it was a string, not an int.
                    print(self.files)
            # specific division
            else:
                hasKey = self.option.lower() in vt_court_division.keys()
                for key, value in vt_court_division.items():
                    if hasKey == True:
                        build_url = baseurl + path + '?' + param1 + str(self.from_year) + "&" + param2 + str(self.to_year) + "&" + param3 + vt_court_division[key] + "&" + param4 + "&" + param5 + str(self.files) + ""
                        # append url to listUrl
                        listURL.append(build_url)
                        # find next
                        break
                    elif hasKey == False:
                        print(''' 
|￣￣￣￣￣￣￣|  

|   ERROR!   |

|＿＿＿＿＿_＿_|

(\__/) || 
(•ㅅ•) || 
/ 　 づ  
                        ''')
                        print('======= Division is invalid, please choose below =======')
                        for i in vt_court_division:
                            print(i)
                        break
        else:
            print('state is invalid')
        
        # return value
        return listURL


# uncomment the code below to test this method
# test = URLGenerator(2014, 2016, "all", 'vermont', 'max' )
# print(test.urlGenerator())
