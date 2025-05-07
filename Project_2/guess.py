from random import randint

r = randint(1, 100)     # Generating random number from 1 to 100

guesses = 0     # Here, guesses = 0. So, I can plus the guesses, whenever the number guess is wrong.

n = -1      # Here, I declare n = -1. So, loop continues till the correct guess.

while(n!=r):
    
    n = int(input("Guess the number: "))    # Takes input from the user

    if(n>r):    
        print("Lower number please! 🔽")    # If number guess is too high
        guesses += 1

    elif(n<r):
        print("Higher number please! 🔼")   # If number guess is too low
        guesses += 1

print(f"Congratulations!🎉 You guess this number correctly '{r}', in {guesses} attempts!")  # If the user guess the number correctly, it prints this.