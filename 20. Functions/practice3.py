#Checking eligible or not for voting using function

#For printing name
def cVoting(fname):
    print("Hello",fname,", please enter your age to check you are eligible for voting or not!")   

#For checking eligibility for voting
def yAge(age):
    if(age>=18):
        print("Your eligible for voting!")
    else:
        print("Your not eligible for voting!")


cVoting(fname = input("Enter your name: ").capitalize())
yAge(age = int(input("")))