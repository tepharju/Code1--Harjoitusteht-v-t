# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:31:31 2021

@author: tepha
Code 1 3.6 Ympyrä
"""

import math

d = float(input("Anna ympyrän halkaisija: "))

r = d/2

ala = math.pi*r**2

keha = 2*math.pi *r

print(f"Ympyrän ala on: {ala}")

print(f"Ympyrän kehän pituus on: {keha}")

