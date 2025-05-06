# Find the sum of digits of a number using recursion.
# Formula: sum(n) = (n % 10) + sum(n // 10)

def sum_of_digits(n):
    if n==0:
        return 0
    else:
        return (n%10) + sum_of_digits(n // 10)
    
print(sum_of_digits(int(input("Enter your two or three digits number: "))))