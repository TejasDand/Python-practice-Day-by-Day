#Syntax:
# def function_name(parameters):
#     pass
#     #Code and Statements


#Finding value of (a+b)^2
def squareAB(a, b):
    square = (a**2)+(2*a*b)+(b**2)
    print(square)

#Calling Function
squareAB(5, 6)



#Finding lesser number by user input
def isLesser (a, b):

    if(a<b):
        print("First number is lesser")
    else:
        print("Second number is lesser or equal to")

isLesser(a = int(input("Enter value of A: ")),
         b = int(input("Enter value of B: ")))