# Random password generator

import string
import random

user_Choice = int(input("Enter your password length: "))
max_Length = 11

def random_Pass():
    pass_Set = string.ascii_letters + string.digits + string.punctuation

    if (user_Choice > max_Length):
        print(f"Max length of password is {max_Length}!")
    
    else:
        for _ in range(user_Choice):
            print(random.choice(pass_Set), end="")


random_Pass()