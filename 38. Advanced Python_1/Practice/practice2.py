# Printing normal table using list comprehension. Number must be entered by a user.

n = int(input("Enter a number: "))

table = [n*i for i in range(1, 11)]
print(table)


# Printing square table:

sq_table = [n*n*i for i in range(1, 11)]
print(sq_table)