def my_decorator(func):
    def wrapper():
        
        print("Something before the function runs.") # First it runs this
        func()  # Then it runs "Hello!"
        print("Something after the function runs.") # Then it runs this after "Hello!"
    
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()