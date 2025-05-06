#To calculate the sum of all the odd numbers within the given range.
given_number = int(input("Enter a number: "))
sum = 0

for i in range(given_number):
    if i%2!=0:
        sum+=i
    
print(sum)