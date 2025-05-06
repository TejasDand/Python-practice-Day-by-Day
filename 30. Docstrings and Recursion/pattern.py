# Printing a pattern:

def pattern(n):
    if(n==0):       #Base Case
        return

    print("*" * n)
    
    pattern(n-1)    #Recursive case - If "n" is 3, first it checks the condition and then print the stars and then minus one. Then it again goes to check condition, it till occurs if n==0 is not happened.

pattern(int(input("Enter a number: ")))