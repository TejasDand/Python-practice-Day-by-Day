#Power of a number:
#if 2^3 = 2*2*2 = 8
#Formula: x * power(x, n-1)

def power(x, n):
    if n==0:
        return 1
    else:
        return x * power(x, n-1) 

print(power(2, 5))