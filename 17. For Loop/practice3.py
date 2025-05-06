#To calculate the sum of all numbers from 1 to a given number.
given_number = int(input("Enter a number: "))
sum = 0

for i in range(1, given_number+1):
    sum+=i

print(sum)