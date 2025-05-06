# Ask the user for two numbers.
# Print their addition using f-string like:

print("Hello, if you want to do addition of two numbers, enter the numbers here:")

n1 = int(input("\nEnter first number: "))
n2 = int(input("\nEnter second number: "))
sum = n1+n2

result = f"\nThe sum of {n1} and {n2} is {sum}."
print(result)