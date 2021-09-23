# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 20:53:47 2021

@author: tepha

Code 1 7.5 Eläimet listaan
"""

elukat = []
ei_listassa = True


while ei_listassa == True:
    
    elain = input("Anna sana:")
    
    if elain not in elukat:
        elukat.append(elain)
    
    else:
        print(f"Sana {elain} on sanottu jo!")
        ei_listassa = False

elukat.sort()
print("Tässä kaikki sanomasi sanat aakkosjärjestyksessä:")

for alkio in elukat:
    print(alkio)

    
