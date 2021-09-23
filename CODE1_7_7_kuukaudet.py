# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:43:07 2021

@author: tepha

CODE1 kuukaudet
"""

lista = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu",
         "toukokuu", "kesäkuu", "heinäkuu", "elokuu",
         "syyskuu", "lokakuu", "marraskuu", "joulukuu"]


while True:

    kk = int(input("Mikä kuukausi: "))
    
    if kk > 12 or kk < 1:
        print("Ei kelpaa!")
    else:
        print(lista[kk-1])
        break

