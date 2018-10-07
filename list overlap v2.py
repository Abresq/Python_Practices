#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 18:11:54 2018

@author: diegoesquivel
"""
import random

a = []
b = []
i = 0
while i < 10:
    a.append(random.randint(1,19))
    b.append(random.randint(1,19))
    i += 1



#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


c = [x for x in set(a) if x in b]

#for elem in a:
#    for elem2 in b:
#        if elem == elem2:
#            x.append (elem)

print (c)
