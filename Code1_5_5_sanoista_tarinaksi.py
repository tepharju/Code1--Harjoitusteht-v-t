# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 11:18:26 2021

@author: tepha
Code 1 5.5 Sanoista tarinaksi
"""

tarina = ""
sanat = 0


while True:
    
    sana = input("Anna sana tarinaan (loppu lopettaa): ")
    
    if sana == "loppu":
        break
    else:
        tarina = tarina + sana + " "
        sanat +=1

if sanat > 50:
    print(tarina)
    print("Olipa hieno tarina!")
elif sanat < 10:
    print(tarina)
    print("Olipa lyhyt juttu..")
    
else:
    print(tarina)

