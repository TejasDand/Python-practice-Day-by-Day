# Type hints are added using the colon (:) syntax for variables and the -> syntax for function return types.


# Variable type hints
a : int = 5
b : int = 6


# Function type hints
def greet(name : str) -> str:
    print(f"Hello, {name}!")

greet("Alice")