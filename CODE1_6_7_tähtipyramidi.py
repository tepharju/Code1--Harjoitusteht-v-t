# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 16:09:10 2021

@author: tepha

CODE1 6.7 Tähtipyramidi
"""

n = int(input("Montako kerrosta tehdään?:"))  # pyramidin kerrosten määrä
rivi = "*"

while n > 0:
    print(" " * n + rivi)
    rivi += "**"
    n -= 1

