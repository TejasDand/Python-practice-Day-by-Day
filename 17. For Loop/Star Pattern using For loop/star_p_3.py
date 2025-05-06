'''
***    Line 1
* *    Line 2
***    Line 3
'''

n = int(input("Enter a number: ")) # 3

for i in range(1, n+1):
    if(i==1 or i==n):               # Printing first line and end line - 1 or 3.
        print("*" * n, end="")

    else:
        print("*", end="")          # 2nd Line - Starting star
        print(" "* (n-2), end="")   # 2nd Line - Middle Space (1 space)
        print("*", end="")          # 2nd Line - Ending star
    print("")