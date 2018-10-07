#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 20:17:13 2018

@author: diegoesquivel
"""
def multiplo_4(numero):
    if int(numero)%4 == 0:
        print("Tu numero es mutiplo de 4")
    else:
        print("tu numero NO es multiplo de 4")

def par_non(numero):
    if int(numero)%2 == 0:
        print("Tu numero es Par")
    else:
        print("Tu numero es Non")



def entra_bien(num1,num2):
    if num1%num2 == 0:
        print("Tus numeros son divisores")
    else:
        print("Tus numeros no son divisores")
