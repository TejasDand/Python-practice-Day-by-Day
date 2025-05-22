check_even = lambda x: "Even" if x%2==0 else "Odd"
square = lambda x: x**2

inp = int(input("Enter a Number: "))

print(f"The number '{inp}' is {check_even(inp)}.")
print(f"The square of this number '{inp}' is: {square(inp)}")