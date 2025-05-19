# importing the statistics module 
from statistics import median 

# Importing fractions module as fr 
from fractions import Fraction as fr 

# positive integers
data_1 = (2, 3, 4, 5, 7, 9, 11) 

# floating integers
data_2 = (2.4, 5.1, 6.7, 8.9)

# fractional numbers
data_3 = (fr(1, 2), fr(44, 12), fr(10, 3), fr(2, 3)) 

# negative numbers
data_4 = (-5, -1, -12, -19, -3) 

# negative & positive numbers
data_5 = (-1, -2, -3, -4, 4, 3, 2, 1) 


# Printing the median of above datasets
print(f"Median of data_1 is: {median(data_1)}")
print(f"Median of data_2 is: {median(data_2)}")
print(f"Median of data_3 is: {median(data_3)}")
print(f"Median of data_4 is: {median(data_4)}")
print(f"Median of data_5 is: {median(data_5)}")