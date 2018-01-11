#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 23:06:32 2018

@author: huyle
"""

from flashtext.keyword import KeywordProcessor
keyword_processor = KeywordProcessor()
keyword_processor.add_keyword('j2ee', 'Java')
keyword_processor.add_keyword('Python')
keyword_processor.extract_keywords('I work on python and j2ee')