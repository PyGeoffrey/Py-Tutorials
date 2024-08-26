# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 10:23:59 2024

@author: LuChen
"""

def greetings():
    q=str(input("Enter a name: "))
    r=str(input("Enter a name: "))
    s=str(input("Enter a name: "))
    t=str(input("Enter a name: "))
    u=str(input("Enter a name: "))
    v=str(input("Enter a name: "))
    w=str(input("Enter a name: "))
    greeter=[q, r, s, t, u, v, w]
    return greeter
greeter=greetings()
for i in range(len(greeter)):
    print("Hi, ", greeter[i])

print("Nice to meet you!")