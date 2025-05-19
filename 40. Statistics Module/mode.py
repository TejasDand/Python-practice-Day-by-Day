# Importing the statistics module 
from statistics import mode 

# Importing fractions module as fr 
# Enables to calculate harmonic_mean of a set in Fraction 
from fractions import Fraction as fr 

# tuple of positive integer numbers 
data1 = (2, 3, 3, 4, 5, 5, 5, 5, 6, 6, 6, 7) 

# tuple of a set of floating point values 
data2 = (2.4, 1.3, 1.3, 1.3, 2.4, 4.6) 

# tuple of a set of fractional numbers 
data3 = (fr(1, 2), fr(1, 2), fr(10, 3), fr(2, 3)) 

# tuple of a set of negative integers 
data4 = (-1, -2, -2, -2, -7, -7, -9) 

# tuple of strings 
data5 = ("red", "blue", "black", "blue", "black", "black", "brown") 


# Printing out the mode of the above data-sets 
print(f"Mode of data set 1 is: {mode(data1)}") 
print(f"Mode of data set 2 is: {mode(data2)}") 
print(f"Mode of data set 3 is: {mode(data3)}") 
print(f"Mode of data set 4 is: {mode(data4)}") 
print(f"Mode of data set 5 is: {mode(data5)}")