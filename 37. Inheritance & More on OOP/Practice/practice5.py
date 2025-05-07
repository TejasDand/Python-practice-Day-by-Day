# Define a class to represent 3D vectors
class Vector:

    # Constructor to initialize vector components
    def __init__(self, i, j, k):
        self.i = i
        self.j = j
        self.k = k


    # Overload the '+' operator to add two vectors
    def __add__(self, other):
        result = Vector(
            self.i + other.i,   # Add corresponding i components
            self.j + other.j,   # Add corresponding j components
            self.k + other.k    # Add corresponding k components
        )
        return result


    # Overload the '*' operator to perform dot product
    def __mul__(self, other):
        result = (
            self.i * other.i +   # Multiply and sum i components
            self.j * other.j +   # Multiply and sum j components
            self.k * other.k     # Multiply and sum k components
        )
        return result


    # Define string representation for printing
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"


# Create vector objects
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
v3 = Vector(7, 8, 9)


# Add two vectors (component-wise addition)
print(v1 + v2)        # Output: Vector(5, 7, 9)

# Multiply two vectors (dot product)
print(v1 * v2)        # Output: 1*4 + 2*5 + 3*6 = 4 + 10 + 18 = 32


print(v2 + v3)        # Output: Vector(11, 13, 15)
print(v2 * v3)        # Output: 4*7 + 5*8 + 6*9 = 28 + 40 + 54 = 32