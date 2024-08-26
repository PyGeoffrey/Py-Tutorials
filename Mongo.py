# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 09:47:48 2024

@author: LuChen
"""

def compute_mongo_age(birthYear, birthMonth, birthDay, currentYear, currentMonth, currentDay):
    '''Computes the age of a resident of Mongo by taking their birthdate and current date and outputs the age, in Mongo years, as a float'''
    
    birth_days=birthYear*390+birthMonth*26+birthDay # calculates the day number at birth
    current_days=currentYear*390+currentMonth*26+currentDay # calculates the current day number
    difference_days=current_days-birth_days # This is the resident's age, in days (difference of the day on birth and the current day)
    difference_years=difference_days/390 # There are 390 days in a year, so we have to divide the age, in days, by 390 to obtain the age, in years.
    return difference_years