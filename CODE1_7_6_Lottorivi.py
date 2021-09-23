# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:48:58 2021

@author: tepha
Code 1 Lottorivi
"""

import random

lista = []

for i in range(7):
    numero = random.randint(1,40)
    lista.append(numero)

print("Tässä lottorivisi:")

for alkio in lista:
    print(alkio)
        

