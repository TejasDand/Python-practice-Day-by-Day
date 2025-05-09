from functools import reduce

l = [1, 2, 3, 4, 5, 6]


# Map Example: Map applies a function to all the items in an input_list
square = lambda x: x*x

sqList = map(square, l)     # Takes two arguements - 1. function name (square) and 2. input list (l)
print(list(sqList))



# Filter Example: Filter creates a list of items for which the function returns true.
def even(n):
    if (n % 2==0):
        return True
    return False

evenList = filter(even, l)      # Takes two arguements - 1. function name (even) and 2. input list (l)
print(list(evenList))



# Reduce Example: Reduce applies a rolling computation to sequential pair of elements.
sum = lambda a,b: a+b

print(reduce(sum, l))       # Takes two arguements - 1. function name (sum) and 2. input list (l)