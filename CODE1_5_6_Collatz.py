# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 10:17:17 2021

@author: tepha

Collatzin konjektuuri
"""

luku = int(input("Anna luku:"))

while luku > 0 and luku != 1:
    
    if luku % 2 == 0:
        luku = luku // 2
        print(luku)
    
    else:
        luku = luku *3 +1
        print(luku)
    
    

