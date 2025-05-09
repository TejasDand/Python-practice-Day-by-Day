# Find maximum number in a list using reduce method:

from functools import reduce

l = [45, 56, 123, 89, 46, 456, 258]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))