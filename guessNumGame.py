# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 16:15:24 2023

@author: micha
"""

#GuessNumGame
#INPUT
#User guess
#PROCESSING
#Loop while the user guess is incorrect
#OUTPUT
#Message to user telling them too low, high, or correct

import random
mynumber=random.randint(1, 10)

#Display a welcome message
print("Welcome to the guess the number game!\n")
userguesses =[] #Empty List
count = 1 #Counter of incorrect guesses

#Loop until correct guess
while True:
    try:
        guess = int(input("Please enter a number between 1 and 10: "))
    except ValueError:
        print("Numbers only please")
        continue
    userguesses.append(guess) #add the guess to the list
    if(guess<mynumber):
        print("Too low")
        count+=1
    elif (guess>mynumber):
        print("Too high")
        count+=1
    elif (guess==mynumber):
        print("You guessed it! It took you ", count," attempts")
        print("You guessed the following numbers: ", userguesses)
        break
        
    
    