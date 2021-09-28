# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:14:16 2021

@author: tepha
Code1 6.5 Sanalaskuri
"""
maara = 0 

sana = input("Anna sana:")
kirjain = input("Mitä kirjainta lasketaan? ")

for i in sana:
    if i == kirjain:
        maara += 1

print(f"Löysin sanasta {sana} {maara} kpl. kirjainta {kirjain}.")


