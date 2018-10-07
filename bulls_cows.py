#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 22:26:09 2018

@author: diegoesquivel
"""
import random

def compare_cowbull(number,guess):
    for i in range(len(number)):
        if number == guess:
            cowbull[0] += 1
        else:
            cowbull[1] += 1

if __name__=="__main__":

    playing = True
    number = str(random.randint(0,9999))
    cowbull=[0,0] #cows,bulls
    guesses = 0


    print("Vamos a jugar a CowBull")
    print("Generare un numero de 4 digitos")
    print("Tendras que adivinar el numero un digito a la vez")
    print("Por cada digito que NO este en su lugar conseguiras un COW y por cada uno que SI este en su lugar reciviras un BULL")
    print("El juego termina cuando recibas 4 BULLS o escribas 'exit'")

    while playing:
        print(number)
        guess = input("Dame tu mejor numero!: ")

        if guess == "exit":
            break

        cowbull_count = compare_cowbull(number,guess)
        guesses =+1

        print("Conseguuiste " + str(cowbull[0]) + " COWS, y " + str(cowbull[1]) + " BULLS.")

        if cowbull[1] == 4:
            print("Haz Ganado, despues de " + str(guesses) + " intentos.")
            playing == False
            break


        else:
            print("Tu numero es Incorrecto, intenta de nuevo.")

#import random
#
#def compare_numbers(number, user_guess):
#    cowbull = [0,0] #cows, then bulls
#    for i in range(len(number)):
#        if number[i] == user_guess[i]:
#            cowbull[1]+=1
#        else:
#            cowbull[0]+=1
#    return cowbull
#
#if __name__=="__main__":
#    playing = True #gotta play the game
#    number = str(random.randint(0,9999)) #random 4 digit number
#    guesses = 0
#
#    print("Let's play a game of Cowbull!") #explanation
#    print("I will generate a number, and you have to guess the numbers one digit at a time.")
#    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
#    print("The game ends when you get 4 bulls!")
#    print("Type exit at any prompt to exit.")
#
#    while playing:
#        print(number)
#        user_guess = input("Give me your best guess!")
#        if user_guess == "exit":
#            break
#        cowbullcount = compare_numbers(number,user_guess)
#        guesses+=1
#
#        print("You have "+ str(cowbullcount[0]) + " cows, and " + str(cowbullcount[1]) + " bulls.")
#
#        if cowbullcount[1]==4:
#            playing = False
#            print("You win the game after " + str(guesses) + "! The number was "+str(number))
#            break #redundant exit
#        else:
#            print("Your guess isn't quite right, try again.")
