#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:50:03 2017

@author: Huy
"""


class URLGenerator:
    def __init__(self, from_year, to_year, option, state, pages):
        self.from_year = from_year
        self.to_year = to_year
        self.option = option
        self.state = state
        self.pages = pages
        
    def urlGenerator(self):
        # VERMONT #
        listURL = []
        """[summary]
            input
                from_year: int
                to_year: int
                option: str 
                    // division name or all
                state: str
                pages: str 
                    // int(str) or "max"/"min"
            ouput
                list of url str
                ["url1", "url2",...]
        """
        vt_court_division = {"civil": "1", "supreme court": "7", "environmental": "3", "family": "4", "criminal": "2"}
        if self.state.lower() == "vermont":
            if self.option.lower() == "all":
                vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F" + str(self.from_year) + "&facet_to_date=01%2F01%2F" + str(self.to_year) + ""
                # return vermont_site_url
                listURL.append(vermont_site_url)
                # find next
                # from 1st url, find next button in soup
                # loup through all next button to add url into list

            else:
                hasKey = self.option.lower() in vt_court_division.keys()
                for key, value in vt_court_division.items():
                    if hasKey == True:
                        vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01/01/" + str(self.from_year) + "&facet_to_date=01/01/" + str(self.to_year) + "&f%5B0%5D=court_division_opinions_library%3A" + vt_court_division[key] + ""
                        # return vermont_site_url
                        listURL.append(vermont_site_url)
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

        return listURL


# uncomment the code below to test this method
            
test = URLGenerator(2014, 2016, "civil", 'vermont', 'max' )
print(test.urlGenerator())
