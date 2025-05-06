# Rock, Paper, Scissor - Game

import random   # Import random module

'''
1 - Rock
2 - Paper
3 - Scissor
'''

computer = random.choice([1, 2, 3])     # Takes random choice from 1, 2 and 3

youStr = input("Enter your choice R/P/S: ").upper()
# By now we have 2 numbers (variables), you and computer


youDict = {"R":1, "P":2, "S":3}
reverseDict = {1: "Rock", 2: "Paper", 3: "Scissor"}


# For taking value of keys "R", "P" and "S"
you = youDict[youStr]


# Printing choice of both players
print(f"Your choice is '{reverseDict[you]}' \nComputer choice is '{reverseDict[computer]}'")


# If computer choice and your choice are equal
if(computer == you):
    print("It's a Draw!")

else:
# Situation for rock, paper and scissor
    if(computer == 1 and you == 2):
        print("You Win!")

    elif(computer == 1 and you == 3):
        print("You Lose!")

    elif(computer == 2 and you == 1):
        print("You Lose!")

    elif(computer == 2 and you == 3):
        print("You Win!")

    elif(computer == 3 and you == 1):
        print("You Win!")

    elif(computer == 3 and you == 2):
        print("You Lose!")
        
    else:
        print("Something Went Wrong !!!")