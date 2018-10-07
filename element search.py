#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 23:55:46 2018

@author: diegoesquivel
"""
a = [2,4,6,8,10,16]

def find1(numero_a_encontrar,list):
    for elemento in list:
        if elemento == numero_a_encontrar:
            return True
    return False

