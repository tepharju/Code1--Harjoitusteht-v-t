# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 12:56:25 2021

@author: tepha
Code1. 8.7 Haluttu monikulmio
"""

import turtle 

polygon = turtle.Turtle()

num_sides = int(input("Montako sivua: "))
side_length = 60
angle = 360.0 / num_sides 

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
    
turtle.done()