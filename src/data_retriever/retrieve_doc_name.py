#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 18:50:03 2017

@author: Huy
"""


class Retriever:
    def __init__(self, from_year, to_year, option):
        self.from_year = from_year
        self.to_year = to_year
        self.option = option
        self.vt_court_division = {"civil": "1", "supreme court": "7", "environmental": "3", "family": "4", "criminal": "2"}
        
    def retriever(self):
        # VERMONT #
        if self.option.lower() == "all":
            vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01%2F01%2F" + str(self.from_year) + "&facet_to_date=01%2F01%2F" + str(self.to_year) + ""
            return vermont_site_url
        else:
            for key, value in self.vt_court_division.items():
                if self.option.lower() == key:
                    vermont_site_url = "https://www.vermontjudiciary.org/opinions-decisions?facet_from_date=01/01/" + str(self.from_year) + "&facet_to_date=01/01/" + str(self.to_year) + "&f%5B0%5D=court_division_opinions_library%3A" + self.vt_court_division[key] + ""
                    return vermont_site_url
#                if self.option.lower() != key:
#                    return "Division " + self.option + " does not exist. "+"There are 5 divisions of Vermont: {}".format(", ".join(self.vt_court_division))


#test = Retriever(2014, 2016, "supreme")
#print(test.retriever())
