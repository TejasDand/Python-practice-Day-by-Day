#Write a program to get days output based on the 1-7 number using match case statement. Here, 1-Monday and 7-Sunday

day = int(input("Enter a number between 1-7: "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("In whole world, there are only 7 days.")