# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 10:45:53 2024

@author: LuChen
"""

try:
    dt=open("C:/Users/LuChen/OneDrive/Documents/Economics Tables.xlsx")
    print(dt)
except SyntaxError as p:
    print(p)
    print("This is an error.")
except PermissionError:
    print("Permission Denied")
except Exception as e:
    print(e)