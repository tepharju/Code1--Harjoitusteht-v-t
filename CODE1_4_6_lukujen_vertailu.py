# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:26:39 2021

@author: tepha
Code 1. 4.6 Lukujen vertailu
"""

eka = int(input("Anna eka luku: "))


toka = int(input("Anna toka luku: "))

if eka == toka:
    print(f"Luvut ovat yhtäsuuret!")
elif eka > toka:
    print(f"Luku {eka} on suurempi!")
elif toka > eka:
    print(f"Luku {toka} on suurempi")