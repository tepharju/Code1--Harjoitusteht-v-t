# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:56:09 2021

@author: tepha

Lukukysely

"""
neg = 0
pos = 0
kpl = 0
summa = 0



while True:
    
    luku = int(input("Kerro luku: (Nolla lopettaa)"))
    
    if luku == 0:
        break
    
    if luku > 0:
        pos += 1
    
    if luku < 0:
        neg +=1
    
    kpl += 1
    summa = summa + luku
    ka = summa / kpl

print(f"syötit {kpl} lukua")
print(f"Lukujen keskiarvo oli: {ka}")
print(f"syötit {neg} kpl. negatiivista lukua")
print(f"syötit {pos} kpl. positiivista lukua")

    
        
    
    

