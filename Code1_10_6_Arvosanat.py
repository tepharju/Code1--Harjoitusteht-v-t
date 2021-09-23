# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:44:52 2021

@author: tepha
Code 1 10.6 Arvosanat
"""

arvosanat = [5,5,5,6,7,7,7,8]

arvosanat2 = [10,9,9,9,8,9]

def keskiarvo(lista:list):
    return (sum(lista)/len(lista))


print(keskiarvo(arvosanat))

print(keskiarvo(arvosanat2))