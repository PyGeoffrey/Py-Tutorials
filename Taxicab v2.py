# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:35:45 2024

@author: LuChen
"""

def FindCab(Cabnumber1, a, b):
    '''findCab(Cabnumber1, a, b) -> bool
    Determines if a number is a cab number. Outputs True or False.
    Cabnumber1, a, b: int
    '''
    boolean=0
    for num3 in range (1, 22):
        #print ("current number 3 is " + str(num3))
        if num3 == a or num3 == b:
            continue # If it is a repeat, skip the number.
        else:
            for num4 in range (num3+1, 21): # Else, find another number that is 1 more than the first number.
                #print ("Evaluting " + str(num3) + " and " + str(num4))
                if num4 == a or num4 == b:
                    continue # If it is a repeat, skip the number.
                elif Cabnumber1 == num3**3 + num4**3:
                    boolean=1 # If it works, return True.
                    print ("Match number found:\n" + str(num3) + " and " + str(num4))
                    return True
    if boolean == 1:
        return True # If it works, return True.
    else:
        return False # Else, return False.

for num1 in range(1, 22): # Number a.
    for num2 in range(num1+1, 22): # Number b.
        cabNum=num1**3+num2**3 # Cabnumber1.
        if cabNum > 1729 and cabNum < 10000: # If it is in range, run the FindCab code.
            if FindCab(cabNum, num1, num2): # If FindCab returns True, print out the number.
                print(cabNum)
                print(num1)
                print(num2)
                