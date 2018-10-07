#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 17:24:25 2018

@author: diegoesquivel
"""

import random



number = random.randint(1,9)
guess = 0
count = 0
    
while guess != number and guess != "exit":
    count += 1
    
    guess = input("Adivina el numero: ")
    
    if guess == "exit":
        break
    
    guess = int(guess)
    
    
    if guess < number:
        print("El numero es mas Grande!")
    elif guess > number:
        print("El numero es mas Pequeño")
    else:
        print("Adivinaste el numero en " + str(count) + " intentos!")
        print("El Numero era: " + str(number) + "!!!")
