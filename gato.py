#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 14:44:04 2018

@author: diegoesquivel
"""



def draw_board():
    i = 0

    horizontal = "--- "
    vertical = "| "

    horizontal = horizontal * 3
    vertical = vertical * (6)

    while i < 4:
        print (horizontal)
        if not (i == 3):
            print (vertical)
        i += 1


draw_board()