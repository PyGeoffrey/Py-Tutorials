# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 20:05:20 2024

@author: LuChen
"""

# Python Class 3960
# Lesson 8 Problem 6
# Author: mathwizard624 (1128611)

import turtle
import random
wn=turtle.Screen()
alex=turtle.Turtle()
all_rolls=[]

def print_result(t, table):
    '''has a turtle draw a background that says:"Roll That Dice!" and print out the results'''
    t.penup()
    t.goto(-150, 150)
    t.write("Let's Roll That Dice!", font=('arial', 25, 'bold'))
    t.goto(0, -150)
    t.write(table, font=('arial', 15, 'normal'))
    
def roll_two_dice():
    '''roll_two_dice() -> int
    computes the sum of two dice rolls
    requires the random module
    '''
    dice1=random.randrange(1,7)
    dice2=random.randrange(1,7)
    return dice1+dice2

def create_chart(inputList, startNumber, endNumber):
    '''create_chart(inputList, startNumber, endNumber) -> str
    creates a chart for a the number of occurences of a number
    inputList: list
    startNumber, endNumber: int
    '''
    outputStr='Number\tOccurence\n------\t---------\n'
    for i in range(startNumber, endNumber+1):
        outputStr+=str(i)+"\t"+str(inputList.count(i))+"\n"
    return outputStr
        
for i in range(10000000):
    all_rolls.append(roll_two_dice())

chart=create_chart(all_rolls, 2, 12)

#print_result(alex, chart)
print(chart)