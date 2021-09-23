# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 13:42:28 2021

@author: tepha
Code1 Nelilaskin funktioilla
"""

def lukujen_summa(luku1,luku2):
    return (luku1+luku2)


def lukujen_erotus(luku1,luku2):
    return (luku1-luku2)

def tulo(luku1, luku2):
    return luku1*luku2

def osamaara(luku1, luku2):
    return luku1 / luku2

def main():
    print("Anna luvut: ")
    
    luku1 = int(input("luku1: "))
    
    luku2 = int(input("luku2: "))
    
    print(lukujen_summa(luku1,luku2))
    
    print(lukujen_erotus(luku1,luku2))

    print(tulo(luku1,luku2))
    
    print(osamaara(luku1,luku2))

main()
