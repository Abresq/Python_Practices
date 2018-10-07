#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 00:24:07 2018

@author: diegoesquivel
"""

counter_dict={}


with open ('nameslist.txt', 'r') as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1

        line = f.readline()


print(counter_dict)
