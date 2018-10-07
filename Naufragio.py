#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 18:46:56 2018

@author: diegoesquivel
"""

nombre = raw_input("Cual es tu nombre? ")

edad = raw_input("Cual es tu edad? ")

agua_necesaria = raw_input("Normlamente cuanta agua consumes en un dia? ")
respuesta_litros= raw_input("Consumes " + agua_necesaria + " litros al dia? ")

if respuesta_litros == "si":
    print("Gracias.")
else:
    agua_necesaria = raw_input("Normlamente cuanta agua consumes en un dia? ")

disponible = raw_input("Cuanta agua tienes disponible en el momento ? (tu respuesta estara en litros) ")
respues_dias = raw_input("Supongamos que estas en un naufragio, cuantos dias estaras en el naufragio? ")

print("normalmente lo minimo que un ser humano necesita de agua para vivir es .08 lts ")

cantidad_necesaria = float(respues_dias) * float(.08)

dias_vividos = float(disponible)/float(cantidad_necesaria)

dias_faltantes = float(respues_dias) - float(dias_vividos)


print("Siento decirte, " + str(nombre) + " pero solo viviras " + str(dias_vividos)+ " dias.")
print("te faltaron " + str(dias_faltantes) + " dias.")
