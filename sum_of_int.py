# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 10:22:20 2024

@author: LuChen
"""

def sum_of_integers(n):
    '''returns the sum of the first n positive integers'''
    total = 0               # running total, initialize at 0

    for i in range(1, n+1): # current number to add, goes from 1 to n
        total += i          # add the current number to our total

    return total            # output the answer