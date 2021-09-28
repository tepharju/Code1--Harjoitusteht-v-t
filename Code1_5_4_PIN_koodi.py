# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 12:55:47 2021

@author: tepha

PIN-koodit
"""

yritykset = 3

pin = 1234

while yritykset != 0:
    
    koodi = int(input("Syötä PIN-koodi: "))
    
    if koodi == pin:
        
        print("Koodi oikein!")
    
    else:
        
        yritykset -= 1
        print("Väärä PIN-koodi")    
        
        print(f"Sinulla on {yritykset} yritystä jäljellä.")


    
    