#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:13:31 2018

@author: diegoesquivel
"""

word = raw_input("Dame una palabra: \n")
rvs = word[::-1]

if word == rvs:
    print("Esto es un Palindromo")
else:
    print("Esto NO es un Palindromo")
