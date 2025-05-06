# Define a class named Number
class Number:

    def __init__(self, n):
        # Constructor that initializes the instance variable 'n'
        self.n = n

    def __add__(self, a):
        # Overloads the + operator
        # This method will be called when you do object1 + object2
        return self.n + a.n  # Adds the 'n' value of both objects

    def __mul__(self, mlt):
        # Overloads the * operator
        # Called when you do object1 * object2
        return self.n * mlt.n  # Multiplies the 'n' values

    def __truediv__(self, div):
        # Overloads the / operator
        # Called when you do object1 / object2
        return self.n / div.n  # Divides the 'n' values

# Create two Number objects
n = Number(4)
m = Number(2)

# Operator overloading in action:
# Calls __add__, __mul__, and __truediv__ respectively
print(n + m)   # 4 + 2 = 6
print(n * m)   # 4 * 2 = 8
print(n / m)   # 4 / 2 = 2.0