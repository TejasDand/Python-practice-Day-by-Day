# Finding the mean of numbers by using statistics module

from statistics import mean

l = []

for i in range(1, 10+1):
    mean_n = int(input(f"Enter the number{i}: "))
    l.append(mean_n)

print(f"The average of list values is: {mean(l)}")