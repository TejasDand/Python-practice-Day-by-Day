# Define a class to represent complex numbers
class Complex:
    
    def __init__(self, i, j):
        # Constructor that initializes the real (i) and imaginary (j) parts
        self.i = i
        self.j = j


    def __add__(self, c2):

        # Overload the '+' operator
        # Adds two complex numbers: (a + bj) + (c + dj) = (a + c) + (b + d)j

        return Complex(self.i + c2.i, self.j + c2.j)
    
    def __mul__(self, c2):

        # Overload the '*' operator
        # Formula: (a + bj) * (c + dj) = (ac - bd) + (ad + bc)j

        real = self.i * c2.i - self.j * c2.j
        imag = self.i * c2.j + self.j * c2.i
        return Complex(real, imag)

    def __str__(self):

        # Define how the object is printed (string representation)

        return f"{self.i} + {self.j}j"
    


# Create two complex number objects
c1 = Complex(1, 2)   # Represents 1 + 2j
c2 = Complex(3, 4)   # Represents 3 + 4j


# Add the complex numbers using overloaded '+' operator
print("Addition:", c1 + c2)     # Output: 4 + 6j

# Multiply the complex numbers using overloaded '*' operator
print("Multiplication:", c1 * c2)  # Output: (1×3 - 2×4) + (1×4 + 2×3)j => -5 + 10j