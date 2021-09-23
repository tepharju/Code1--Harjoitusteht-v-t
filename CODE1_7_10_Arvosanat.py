# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:57:55 2021

@author: tepha
Code 1 7.10 Arvosanat
"""

arvosanat = []

while True:

    num = int(input("Anna aineen arvosana (0 lopettaa): "))
    
    if num == 0:
        print("Ohjelma loppuu...")
        break
    
    else:
        arvosanat.append(num)
    
ka = round(sum(arvosanat)/len(arvosanat),2)

print(f"Suurin arvosana: {max(arvosanat)}")    

print(f"Pienin arvosana: {min(arvosanat)}")

print(f"Keskiarvo: {ka}")    
    
