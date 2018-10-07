#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:53:04 2018

@author: diegoesquivel
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

num = raw_input("Dame un Numero: ")
for element in a:
    if element <= int(num):
        b.append(element)

print(b)
