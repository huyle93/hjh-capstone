#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 10:34:32 2018

@author: Huy
"""

from nameparser import HumanName
name = ["Thomas Durkin", "John Zaikowski", "Michelle Slack", "Anthony Gildersleeve"]
resultName = []
for i in name:
     eachName = HumanName(i)
     nameObject = {}
     nameObject['firstname'] = eachName.first
     nameObject['lastname'] = eachName.last
     resultName.append(nameObject)

print(resultName)
# print(name.as_dict())
# print(name.first, name.last)

# Output
# [{"firstname": "name", "lastname":"name"},{},{}]