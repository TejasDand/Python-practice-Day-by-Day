#Write a program to calculate values by using match case statment.

num1 = int(input("Enter first number value: "))
num2 = int(input("Enter second number value: "))
opr = input("Enter operator: ")

match opr:
    case "+":
        print("Addition of two values is:", num1+num2)
    case "-":
        print("Subtraction of two values is:", num1-num2)
    case "*":
        print("Multiplication of two values is:", num1*num2)
    case "/":
        print("Division of two values is:", num1/num2)