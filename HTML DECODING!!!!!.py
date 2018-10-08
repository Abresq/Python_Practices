#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 02:04:45 2018

@author: diegoesquivel
"""


import requests
from bs4 import BeautifulSoup

titulos = []

url = "https://www.nytimes.com"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

tittles = soup.find_all("div", class_="css-k8gosa esl82me3")

for tittle in tittles:
    print(tittle.text)

