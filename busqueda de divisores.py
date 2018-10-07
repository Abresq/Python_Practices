#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 21:53:04 2018

@author: diegoesquivel
"""


num = int(raw_input("Ingresa un numero: ")) + 1
a = range(1,int(num))
b= []

for elem in a:
    if num % elem == 0:
        b.append(elem)
        
print (b)