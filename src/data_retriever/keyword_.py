#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:30:02 2018

@author: huy
"""
from collections import Counter
from flashtext.keyword import KeywordProcessor
keyword_processor = KeywordProcessor()

class Keyword:
    def __init__(self, keyword, data):
        self.keyword = keyword
        self.data = data
        
    def hasKeyword(self):
        keyword_processor.add_keyword(self.keyword)
        result = keyword_processor.extract_keywords(self.data)
        if len(result) > 0:
            return True, Counter(result)
        else:
            return "NOPE"
    
#test = Keyword('Attorney','Hello Attorney')    
#print(test.hasKeyword())