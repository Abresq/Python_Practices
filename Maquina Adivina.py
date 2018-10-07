#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 15:28:08 2018

@author: diegoesquivel
"""

import random

def ask_input():
    a_b = input("El numero que puenso es " + guess + " , es correcto o es mas alto o mas bajo?: ")

print("Piensa en un numero, y yo intentare de adivinarlo")
listo = input("Estas listo?: ")
if listo == "si" or "SI" or "Si":
    guess = str(50)
    ask_input()
    if a_b == "correct":
        print("Perfecto!, lo Adivine!")
    elif a_b == "mas alto":
        guess = random.randint(guess,100)
        print(guess)
        ask_input()
    else:
        guess = random.randint(0,guess)
        print(guess)
        ask_input()
