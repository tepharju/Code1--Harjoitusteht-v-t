# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 07:53:10 2021

@author: tepha
Code1 6.4 Saippuakauppias
"""

sana = str(input("Anna sana: "))

nurinkurin = sana[::-1]

if sana == nurinkurin:
    print("sanasi on palindromi!")

else:
    print("sanasi ei ole palindromi!")