# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:25:41 2021

@author: tepha
"""
d = {}

eka = int(input("Anna eka luku:"))

vika = int(input("Anna vika luku:"))


for i in range(eka, vika+1):
    
    kymmen = i*10
    d[i] = kymmen

print(d)
    
    
    

