#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:56:55 2018

@author: diegoesquivel
"""


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

# print(len(a))
# print(len(b))

for num in a:
    if num in b:
        if num not in c:
            c.append(num)

print(c)

