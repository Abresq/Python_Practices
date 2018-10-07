#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 00:30:05 2018

@author: diegoesquivel
"""

frase_ini = raw_input("Dame una frase y te la volteo!: ")
frase_split = frase_ini.split( )
frase_rvs = frase_split[::-1]
frase_join = " ".join(frase_rvs)

print(frase_join)
