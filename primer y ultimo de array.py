#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 22:43:47 2018

@author: diegoesquivel
"""
import random
x = []
i = 0

while i<=10:
    x.append(random.randint(0,10))
    i += 1


def list_ends(list):
    return (list[0],list[-1])
