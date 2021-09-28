# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:06:21 2021

@author: tepha
Code 1. 8.8 Lumihiutale
"""

import turtle 

p = turtle.Turtle()
p.speed(100)


for i in range(50):
  p.forward(100)
  p.right(10)
  p.forward(10)
  p.left(20)
  p.forward(50)
  p.penup()
  p.goto(0,0)
  p.pendown()

    
turtle.done()