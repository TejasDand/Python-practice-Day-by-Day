#Write a program to display the last digit of a number and then check whether the last digit of a number (entered by user) is divisible by 3 or not.

num = int(input("Enter a two or three digit number: "))

ld = num % 10
    
if(ld%3 == 0):
    print("Last digit number is divisible by 3.")
else:
    print("Last digit number is not divisible by 3.")