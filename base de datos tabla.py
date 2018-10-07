#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 22:27:40 2018

@author: diegoesquivel
"""

import numpy as np
import pandas as pd

n = 5

i = 0

lista = [""]
while i <= n:
    b = input("inserte nombre: ")
    lista.append(b)
    i+=1
A = np.array(lista)
print(lista)

i = 1
lista = [""]
while i <= n:
    b = input("Inserte edad: ")
    lista.append(b)
    i+=1
B= np.array(lista)
print (lista)

bd = {"Nombre": A, "Edad": B}
BD = pd.DataFrame(data=bd)
