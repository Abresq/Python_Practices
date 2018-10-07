#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 22:24:55 2018

@author: diegoesquivel
"""


def iniciar_juego():
    respuestausr1 = input("%s, quieres escojer: Piedra, Papel o Tijera; " % user1)
    respuestausr2 = input("%s quieres escojer: Piedra, Papel o Tijera: " % user2)


    def comparar(u1,u2):
        if u1 == u2:
            print("Empataron!")

        elif u1 == "piedra":
            if u2 == "tijeras":
                print(user1 + " Gano!")
            else:
                print(user2 + " Gano!")

        elif u1 == "tijeras":
            if u2 == "papel":
                print(user1 + " Gano!")
            else:
                print(user2 + " Gano!")

        elif u1 == "papel":
            if u2 == "piedra":
                print(user1 + " Gano!")
            else:
                print(user2 + " Gano!")
        else:
            print("Sus respuestas no son validas!")

    comparar(respuestausr1,respuestausr2)

    NG = input("Quieren iniciar un nuevo juego?: ")
    if NG == "si":
        iniciar_juego()
    else:
        print("Gracias por jugar: " + user1 + ", "+ user2 + ".")




user1 = input("Usuario 1, Cual es tu nombre?: ")
user2 = input("Usuario 2, Cual es tu nombre?: ")

NG = input("Quieren iniciar un nuevo juego?: ")
if NG == "si":
    iniciar_juego()
else:
    print("Gracias por jugar: " + user1 + " y "+ user2 + ".")
