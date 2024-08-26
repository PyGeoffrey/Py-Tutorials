# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 09:35:38 2024

@author: LuChen
"""

import random
correctAnswer = random.randrange(1, 3)


def guessNum(guess, correctAnswer):
    '''gathers a guess and correct answer, and prints if the guess is too high, to low, or exactly equal to the correct answer. It also return True if the number was guessed right and false otherwise.'''
    if guess > correctAnswer:
        print("Sorry,", guess, "is too high.")
        return False
    elif guess < correctAnswer:
        print("Sorry,", guess, "is too low.")
        return False
    else:
        print("Good job!", correctAnswer, "is my number.")
        return True

def guessingGame(correctAnswer):
    '''asks the user for a number and executes guessNum function until the user guesses correctly.'''
    guessedCorrect=False
    guesses=0
    while guessedCorrect==False:
        guessedCorrect = guessNum(int(input("Enter your guess: ")), correctAnswer)
        guesses+=1
    print("It took you", guesses, "guesses.")


        
print("I'm thinking of a number between 0 and 100")
guessingGame(correctAnswer)