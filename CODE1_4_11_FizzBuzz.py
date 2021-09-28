# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 10:54:23 2021

@author: tepha
Code1 4.11 Fizzbuzz!
"""

luku = int(input("Anna luku: "))

if luku % 5 == 0 and luku % 3 == 0:
    print("FizzBuzz!")
elif luku % 5 == 0:
    print("Buzz!")
elif  luku % 3 == 0:
    print("Fizz!")

