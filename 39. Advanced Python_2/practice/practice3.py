# Filter a list of numbers which are divisible by 5:

n = [1, 2, 5, 6, 10, 15, 20, 21, 23, 30]

def div(n):
    if (n % 5 == 0):
        return True
    return False

result = list(filter(div, n))
print(result)