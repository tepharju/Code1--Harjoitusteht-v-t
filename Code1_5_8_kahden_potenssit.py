# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 13:06:46 2021

@author: tepha

kahden potenssit
"""

n = 0
pot = 0
seuraava = 0

raja = int(input("Mihin asti lasketaan?"))

while seuraava < raja:
    pot = 2**n
    seuraava = 2**(n+1)
    print(pot)
    n +=1
