#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 23:12:52 2018

@author: diegoesquivel
"""

def fibonacci():
    num = int(input("Cuantos numeros quieres generar?: "))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())
