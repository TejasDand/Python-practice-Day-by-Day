# Divide a & b. If b=0 display infinite using try-except block (ZeroDivisionError):

try:
    a = int(input("Enter value of A: "))
    b = int(input("Enter value of B: "))
    print(a/b)

except ZeroDivisionError as z:
    print("Infinite!")