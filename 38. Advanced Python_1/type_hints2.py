# Advanced Type Hints

# typing module provides more advanced type hints, such as List, Tuple, Dict and Union. Like this,
from typing import List, Tuple, Dict, Union

# List of integers
numbers : List[int] = [1, 2, 3, 4, 5]

# Tuple of a string and an integer
person : Tuple[str, int] = ("Alice", 30)

# Dictionary with string keys and integer values
scores : Dict[str, int] = {"Tejas":18, "Aayush":20}

# Union type for variables that can hold multiple values
identifier : Union[int, str] = "ID123"
identifier = 12345  # Also Valid