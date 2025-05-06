#Sum of natural numbers:
#if n=5 - 5+4+3+2+1 = 15
#Formula: n + sum(n-1)

def sum(n):
    if n==0:
        return 0
    else: 
        return n + sum(n-1)

print(sum(int(input("Enter your number: "))))