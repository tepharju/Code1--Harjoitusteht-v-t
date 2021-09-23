# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:52:53 2021

@author: tepha
Code 1 7.9 Lisää listaan
"""

luvut = []

n = int(input("Montako lukua lisätään: "))

for i in range(n):
    luku = int(input("Anna luku: "))
    luvut.append(luku)

for alkio in luvut:
    print(alkio)
    

