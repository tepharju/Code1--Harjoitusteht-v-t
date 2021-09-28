# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:24:29 2021

@author: tepha
Code1 3.3 Nimi ja ikä
"""
nimi = input("Kerro nimesi: ")

ika = int(input("Kerro ikäsi: "))

vuosi = 2021 - ika

elo = ika * 365 * 24 * 3600

print(f"Hei {nimi}! Olet syntynyt vuonna {vuosi} ja olet ollut elossa {elo} sekuntia.")

