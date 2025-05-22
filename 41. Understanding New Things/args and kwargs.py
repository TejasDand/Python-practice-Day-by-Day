# Define a function that accepts any number of positional and keyword arguments

def fun(*args, **kwargs):
    
    # Print the tuple of all positional arguments
    print(f"Args: {args}")
    
    # Print the dictionary of all keyword arguments
    print(f"Kwargs: {kwargs}")

# Call the function with some positional and keyword arguments
fun(1, 2, 3, name="Arin", age=21)