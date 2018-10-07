#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:21:45 2018

@author: diegoesquivel
"""

import requests
from bs4 import BeautifulSoup

def get_text(url):


    url1 = str(url)

    r = requests.get(url1)

    soup = BeautifulSoup(r.content,'html.parser')

    text = soup.find_all("p")

    file_name=input("Que nombre quieres para tu archivo?")
    
    with open(file_name+'.txt','w') as open_file:

        for elem in text:
            open_file.write(elem.text)


get_text("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
