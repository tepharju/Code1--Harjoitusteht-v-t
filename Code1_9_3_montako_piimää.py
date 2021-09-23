# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:35:58 2021

@author: tepha
CODE1. Montako purkkia piimää?
"""

sanalista = [
  "banaani", "maito", "olut", "juusto", "piimä", "mehu", "makkara",
  "tomaatti", "kurkku", "voi", "margariini", "juusto", "makkara",
  "olut", "piimä", "piimä", "voi", "olut", "suklaa"
]

sanat = {}

for sana in sanalista:
    
    if sana not in sanat:
        sanat[sana] = 0
    
    sanat[sana] +=1

print(sanat)


