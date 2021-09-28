# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:28:25 2021

@author: tepha
Code 1 3.5 Ruokakustannukset
"""

lounas_n = int(input("Montako kertaa viikossa syöt työpaikkalounasta? ")) 

lounas_hinta = float(input("Lounaan hinta? ")) 

ostokset = float(input("Paljonko käytät viikossa ruokaostoksiin? ")) 

viikossa = ostokset + lounas_n * lounas_hinta 

print("Kustannukset keskimäärin:") 

print("Päivässä", round(viikossa / 7,3), "euroa") 

print("Viikossa", round(viikossa,3), "euroa")
