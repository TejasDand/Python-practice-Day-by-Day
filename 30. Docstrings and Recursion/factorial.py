#factorial (5) = 5*4*3*2*1

def factorial(n):
    '''Here, n takes input from the user. Through n, we find the factorial of a given number enter by the user. If user inputs the 0 or 1 it return value 1. Otherwise, it performs else part where we call the function inside the function.'''
    
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(int(input("Enter a number to do find factorial: "))))
# print(factorial.__doc__)