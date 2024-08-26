# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 11:46:28 2024

@author: LuChen
"""

# Python Class 3960
# Lesson 5 Problem 7 part (b)
# Author: mathwizard624 (1128611)

def is_multiple(x, y):
    '''is_multiple(x, y) -> bool
    returns True if x is a multiple of y, False otherwise
    x, y: int
    '''
    # check if y divides evenly into x
    return (x % y == 0)

def sum_of_proper_divs(n):
    '''sum_of_proper_divs(n) -> int
    returns the sum of all proper divisors of n
    n: int
    '''
    total=0
    for divisor in range(1, n):
        if is_multiple(n, divisor):
            print(divisor)
            total+=divisor
    return total
print(sum_of_proper_divs(496))

for i in [1, 2, 4, 8, 16, 31, 62, 124, 248]:
    print(is_multiple(496, i))