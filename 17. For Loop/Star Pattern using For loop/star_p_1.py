'''
  *
 ***
*****
'''

n = int(input("Enter a number: ")) # Suppose, if we enter a number: 3

for i in range(1, n+1): # n+1=4, but range by default do this (n-1). So, n-1 = 4-1 = 3.
   
    print(" " * (n-i), end="") # For printing space, n-i = 3-1=2, 3-2=1, 3-3=0
    
    print("*" * (2*i-1), end="") #For printing stars, 2*i-1 = 2*1-1=1, 2*2-1=3, 2*3-1=5 

    print("") # For space