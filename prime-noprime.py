#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:28:28 2018

@author: diegoesquivel
"""

num = int(raw_input("Inserta un numero: "))

a = [x for x in range(2,num) if num % x == 0]
if num > 1:
    if len(a)==0:
        print("Primo")
    else:
        print("No Primo")

