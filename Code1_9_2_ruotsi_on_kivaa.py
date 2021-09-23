# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 21:33:00 2021

@author: tepha
CODE1. 9.2 Ruotsi on kivaa
"""

sanakirja = {"iso":"stor", "pieni":"lilla", "kaunis":"vackert", "ohjelmointi":"programmering"}

suomi = input("Anna sana suomeksi: ")

if suomi in sanakirja:
    
    print(suomi+" on ruotsiksi "+sanakirja[suomi])

else:
    print("En tiedä sanaa "+suomi+ " ruotsiksi!")