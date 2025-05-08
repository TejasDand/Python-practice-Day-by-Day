# Try - Except Block:

# try:
#     a = int(input("Enter a number: "))
#     print(a)

# except ValueError as v:
#     print(v)

# except Exception as e:
#     print(e)

# print("Thank You!")



# Raising Custom Errors:

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

if b == 0:
    raise ZeroDivisionError("It is not possible to divide any number by zero!")
else:
    print(f"The division of a/b is {a/b}")