#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 23:14:24 2018

@author: huyle
"""
from io import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os

class Converter:
    def __init__(self, pdfDir, txtDir):
        self.pdfDir = pdfDir
        self.txtDir = txtDir
    #converts pdf, returns its text content as a string
    def convert(self, fname, pages=None):
        if not pages:
            pagenums = set()
        else:
            pagenums = set(pages)
    
        output = StringIO()
        manager = PDFResourceManager()
        converter = TextConverter(manager, output, laparams=LAParams())
        interpreter = PDFPageInterpreter(manager, converter)
    
        infile = open(fname, 'rb')
        for page in PDFPage.get_pages(infile, pagenums):
            interpreter.process_page(page)
        infile.close()
        converter.close()
        text = output.getvalue()
        output.close
        return text 
    
    #converts all pdfs in directory pdfDir, saves all resulting txt files to txtdir
    def convertMultiple(self):
        if self.pdfDir == "": self.pdfDir = os.getcwd() + "\\" #if no pdfDir passed in 
        if len(os.listdir(self.pdfDir)) == 0: 
            print("Empty folder")
        for pdf in os.listdir(self.pdfDir): #iterate through pdfs in pdf directory
            fileExtension = pdf.split(".")[-1]
            if fileExtension == "pdf":
                pdfFilename = self.pdfDir + pdf 
                
                text = self.convert(pdfFilename) #get string of text content of pdf
                textFilename = self.txtDir + pdf + ".txt"
                textFile = open(textFilename, "w") #make text file
                textFile.write(text) #write text to text file

#pdfDir = "../../data/raw/"
#txtDir = "../../data/interim/"
#converter = Converter(pdfDir,txtDir)
#converter.convertMultiple()