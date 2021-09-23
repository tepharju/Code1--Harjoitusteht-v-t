# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:38:14 2021

@author: tepha
Code 1. 10.4 Suurin luku
"""

def suurin(a,b,c):
    if a > b and a > c:
        return a
    if b > a and b > c:
        return b
    if c > a and c > b:
        return c
    else:
        return 0

print(suurin(1,2,3))

print(suurin(9,111,2))

print(suurin(3,2,3))

