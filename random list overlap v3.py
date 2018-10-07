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

c = [x for x in set(a) if x in b]

print (c)
