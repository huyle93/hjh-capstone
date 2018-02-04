#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:50:03 2017

@author: Huy
"""


class URLGenerator:
    def __init__(self, from_year, to_year, option, state):
        self.from_year = from_year
        self.to_year = to_year
        self.option = option
        self.state = state
        
    def urlGenerator(self):
        # VERMONT #
        vt_court_division = {"civil": "1", "supreme court": "7", "environmental": "3", "family": "4", "criminal": "2"}
        if self.state.lower() == "vermont":
            if self.option.lower() == "all":
                vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F" + str(self.from_year) + "&facet_to_date=01%2F01%2F" + str(self.to_year) + ""
                return vermont_site_url
            else:
                hasKey = self.option.lower() in vt_court_division.keys()
                for key, value in vt_court_division.items():
                    if hasKey == True:
                        vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01/01/" + str(self.from_year) + "&facet_to_date=01/01/" + str(self.to_year) + "&f%5B0%5D=court_division_opinions_library%3A" + vt_court_division[key] + ""
                        return vermont_site_url
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


# uncomment the code below to test this method
            
#test = URLGenerator(2014, 2016, "civil", 'vermont')
#print(test.urlGenerator())
