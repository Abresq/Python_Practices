#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 00:45:24 2018

@author: diegoesquivel
"""
import random
import string

longitud = int(input("Que longitud quieres para tu contrasena?: ")) #Dice que tan larga sera la contraseña
pwd = "" #declaro la variablñe de password
count = 0 #declaro count para iniciar una cuenta desde 0
while count != int(longitud): #mientras que count no sea igual a la longitud que especifique, se seguira corriendo el codigo

    letters = [random.choice(string.ascii_letters)] #escoje una letra con esta "funcion"
    digits = [random.choice(string.digits)] #escoje un numero con esta "funcion"
    punctuation = [random.choice(string.punctuation)]#escoje un signo con esta "funcion"
    everything = letters + digits + punctuation # une la letra numero y signo en una lista

    pwd += random.choice(everything) # agrega los caracteres cada vez que se corra el codigo, es decir hasta que el count se apague
    count += 1 #aumenta el count hasta que llegue a la longitud especificada



if count == longitud: # si el count es igual a la longitud se imprimia la contraseña
        print (pwd)
