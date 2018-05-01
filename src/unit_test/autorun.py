#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  1 02:16:30 2018

@author: Huy
"""

import requests
from bs4 import BeautifulSoup

from datetime import datetime, timedelta

def n_booking(n):
    # start tomorrow
    bk = (datetime.now() + timedelta(days=1))
    # check next n days
    for i in range(n): 
        mon, day, year = bk.month, bk.day, bk.year
        # go to next day
        bk = (datetime.now() + timedelta(days=1))
        d_mon, d_day, d_year = bk.month, bk.day, bk.year
        url ="http://hotelname.com/arrivalDate=d{mon}%2F{day}%2F{year}**&departureDate={d_mon}%2F{d_day}%2F{d_year}"\
            .format(mon=mon, day=day, year=year, d_day=d_day, d_mon=d_mon,d_year=d_year)
        wb_data = requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        names = soup.select('.PropertyName')
        prices = soup.select('.RateSection ')
        for name,price in zip(names,prices):

             yield  {
                "name":name.get_text(),
                "price":price.get_text()
              }