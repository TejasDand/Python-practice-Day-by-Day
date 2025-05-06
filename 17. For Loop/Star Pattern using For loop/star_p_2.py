'''
*
**
***
****
*****
'''

n = int(input("Enter a number: ")) # Suppose, if we take a number: 5

for i in range(1, n+1):

    print("*" * i, end="") # It prints star based on iteration, like 1 prints *, 2 prints **, 3 prints *** and so on.

    print("") # For space.