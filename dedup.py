#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 00:22:15 2018

@author: diegoesquivel
"""

a = [1, 2, 3, 4, 5, 6, 7, 4, 8, 10, 9, 10, 11, 12, 13]
y=[]

def dedup(x):
    for elem in x:
        if elem not in y:
            y.append(elem)
            

def dedupv2(x):
    return(list(set(x)))

    
