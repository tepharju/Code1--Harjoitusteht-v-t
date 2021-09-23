# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 21:01:52 2021

@author: tepha

Code 1. 7.7 Lista uusiksi
"""

valmis_lista = [1,2,3,4,5]

print(valmis_lista)

while 1+1==2:

    indeksi = int(input("Anna indeksi: "))
    
    if indeksi == -1:
        break
    
    else:
        uusi = int(input("Anna uusi arvo:"))
        
        valmis_lista[indeksi] = uusi
        
        print(valmis_lista)

print("Joko lopetit?")