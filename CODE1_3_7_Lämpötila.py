# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:35:53 2021

@author: tepha
Code 1 3.6 Lämpötilat
"""

while True:

    c = float(input("Anna lämpötila celsius-asteina: "))
    
    if c < -273.15:
        print("Ei mahdollista!")
    
    else:
        k = c + 273.15
        f = 1.8 * c + 32
        
        print(f"Kelvineinä: {k}")
        print(f"Fahrenheit: {f}")
        
        break
        
        
        

