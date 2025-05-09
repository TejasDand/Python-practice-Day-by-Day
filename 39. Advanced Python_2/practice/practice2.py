# Print tables in a vertical string:

n = int(input("Enter a number: "))
table = [str(n*i) for i in range(1, 11)]

s = "\n".join(table)
print(s)