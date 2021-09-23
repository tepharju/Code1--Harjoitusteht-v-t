# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 17:30:01 2021

@author: tepha
CODE1 7.11 valmis lista
"""

lista = [932, 168, 876, 250, 426, 231, 554, 105, 888, 684, 639, 131, 140, 382, 479, 402, 125, 264, 286, 290, 205, 944, 761, 735, 611, 646, 908, 438, 852, 937, 397, 503, 591, 736, 734, 124, 434, 952, 269, 13, 164, 161, 128, 170, 646, 200, 331, 946, 590, 973, 569, 784, 778, 358, 463, 712, 283, 357, 959, 598, 518, 853, 305, 767, 44, 135, 175, 407, 677, 749, 714, 517, 766, 346, 488, 687, 338, 375, 341, 582, 912, 389, 224, 326, 561, 106, 756, 709, 445, 106, 727, 258, 671, 48, 857, 69, 171, 840, 335, 696]

#Listan lukujen summa

summa = 0
for alkio in lista:
    summa += alkio
    
print(summa)

#parillisten summa

sum_par = 0
pariton = 0

for alkio in lista:
    if alkio % 2 == 0:
        sum_par += alkio
    else:
        pariton += alkio
print(sum_par)
print(pariton)

#Listan suurin ja pienin

print(max(lista))

suurin = lista[0]
pienin = lista[0]

for luku in lista:
    if luku > suurin:
        suurin = luku
print(suurin)

for a in lista:
    if a < pienin:
        pienin = a
print(pienin)