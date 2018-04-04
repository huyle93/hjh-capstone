# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 17:15:37 2018

@author: Huy
"""
from os import listdir
from os.path import isfile, join
from os import path
import sys
import PyPDF2
# using PyPD2 for pdf metadata

# this def takes the dir path
# this def returns total size of files (exclude hidden) in the dir


def getDirectorySize(mypath):
#    mypath = '../../data/raw/'
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) if not f.startswith('.')]
    numsize = 0
    for i in onlyfiles:
        fname = path.expanduser(mypath + i)
        size = path.getsize(fname) / 1000000
        numsize += size
    return '{0:.2f} MB'.format(numsize)


print(getDirectorySize('../../data/raw/75/'))
    
def printArt(text):
    from colorama import init
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    from termcolor import cprint 
    from pyfiglet import figlet_format
    
    cprint(figlet_format(text, font='starwars'),
           'yellow', 'on_red', attrs=['bold'])
    
