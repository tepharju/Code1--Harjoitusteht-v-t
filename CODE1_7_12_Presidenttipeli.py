# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:48:40 2021

@author: tepha

CODE1 7_11 Presidentipeli
"""

lista = ["Ståhlberg", "Relander", "Svinhufvud",
         "Kallio", "Ryti", "Mannerheim",
         "Paasikivi", "Kekkonen", "Koivisto",
         "Ahtisaari", "Halonen", "Niinistö"]

print("Tervetuloa presidenttipeliin!")

pisteet = 0

while pisteet < 12:
   
    nimi = input("Nimeä Suomen presidentti: ")
    
    if nimi == "":
        break
    
    if nimi in lista:
        pisteet += 1
        print("Hyvä! Tiesit!")
        lista.remove(nimi)
    else:
        print("Ei kelpaa!")

print(f"Muistit {pisteet} presidenttiä.")

if len(lista) != 0:
    print("Näitä et vielä muistanut:")
    for k in lista:
        print(k)