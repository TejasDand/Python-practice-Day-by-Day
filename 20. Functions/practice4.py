# Write a Python function to find the maximum of three numbers.

def maximum(a,b,c):
    
    #If a is greater than both values
    if(a>b and a>c):
        return a

    #If b is greater than both values    
    elif(b>a and b>c):
        return b

    #If c is greater than both values    
    else:
        return c

a = int(input("Enter value of A: "))
b = int(input("Enter value of B: "))
c = int(input("Enter value of C: "))

print(maximum(a, b, c))