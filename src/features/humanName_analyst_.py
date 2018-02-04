#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:34:32 2018

@author: Huy
"""

from nameparser import HumanName
name = HumanName("Jane s Hillyard")
print(name.as_dict())
print(name.first, name.last)