# -*- coding: utf-8 -*-
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import os, fnmatch
import re
import sys
import shutil
import csv

class converter:
    def convert_pdf_to_txt(path):
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        fp = file(path, 'rb')
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        password = ""
        maxpages = 0
        caching = True
        pagenos=set()
    
        for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
            interpreter.process_page(page)
    
        text = retstr.getvalue()
    
        fp.close()
        device.close()
        retstr.close()
        return text
    
    # dirs for process:
    #polfolder = {"Direct Hit Documents" , "Manual Add Docs", "Wildcard Searches"}
    polfolder = {"Wildcard Searches"}
    for d in polfolder:
        sourcedir = r"folderdir" + d + "\\"
        targetdir = r"folderdir" + d + "\liability\\"
        convertdir = r"folderdir" + d + "\converted\\"
    
        srcfilenames=fnmatch.filter(os.listdir(sourcedir), '*.pdf')
    
        for i in srcfilenames:
            fin = sourcedir + i
            converted = convert_pdf_to_txt(fin)
            fout = convertdir + i[:i.index(".")] + ".txt"
            txtout = open(fout,'w')
            txtout.write(converted)
    
        #print ("files converted : ",os.listdir(convertdir))
    
        #os.chdir( "c://Users/n0050494/Documents/pol_type")
        words = {'Coverage E - Personal Liability',
                'Coverage F – Medical Payments',
                'Definitions'}
    
        os.chdir( convertdir)
        filenames = os.listdir('.')
        liab = []
    
        for i in filenames:
            for word in words:
                if re.search(r'\b' + word + r'\b', open(i).read()):
                    liab.append(i)
    
        # remove dups:
        liabilityfiles = []
        [liabilityfiles.append(x) for x in liab if x not in liabilityfiles]
    
    
        # test for missing files non liability
    
        fileSet = os.listdir(convertdir)
        nonliab =[name for name in fileSet if name not in liabilityfiles]
    
        # write out files to excel
        with open("homedir/nonLiab" + d + ".csv","w") as fp:
            wr = csv.writer(fp, dialect='excel', lineterminator = '\n')
            for i in nonliab:
                wr.writerow([i])
    
        with open("homedir/liab" + d + ".csv","w") as fp:
            wr = csv.writer(fp, dialect='excel', lineterminator = '\n')
            for i in liabilityfiles:
                wr.writerow([i])
    
        #copy to liability file
        # adding exception handling
    
    
        for i in liabilityfiles:
            fname = i[:i.index(".")] + ".pdf"
            try:
                shutil.copy(sourcedir + fname, targetdir)
            except IOError as e:
                print("Unable to copy file. %s" % e)
            except:
                print("Unexpected error:", sys.exc_info())
    
    #Copy files with Liab
