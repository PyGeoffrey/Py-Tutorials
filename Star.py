# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 20:08:22 2024

@author: LuChen
"""

# Python Class 3960
# Lesson 3 Problem 6
# Author: mathwizard624 (1128611)

import turtle
wn=turtle.Screen
alex=turtle.Turtle()
alex.speed(1000000)
a=int(input("Enter a number: "))
turn=180/a
bigTurn=180-turn
for i in range (a):
    alex.forward(100)
    alex.left(180-turn)