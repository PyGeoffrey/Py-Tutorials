# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 11:47:12 2024

@author: LuChen
"""


import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
for i in range(1,990000):
    ai = turtle.Turtle()    # Create a turtle, assign to alex
    ai.speed(2000000000000000000000000000000000000^1000000000000000000000000000000)
    ai.left(1+((1/4)*i))             # Tell alex to turn left by 90 degrees
    ai.forward(90) #ai.forward(30+((1/8)*i))           Complete the second side of a rectangle

wn.mainloop()             # Wait for user to close window