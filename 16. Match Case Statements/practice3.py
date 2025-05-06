#Write a program to check whether you can drive or not using match case statement.

age = int(input("Enter your age: "))

match age:
    case _ if(age<18):
        print("You cannot drive!")

    case _ if(age>=18 and age<=50):
        print("You can drive.")

    case _ if(age>50 and age<=80):
        print("You can drive, but be cautious.")

    case _ if(age>80):
        print("Ghar pe betho or aaram karo, Kaka!")