# Add static method greet the user hello.

# Making Calculator to find the square, cube and squareRoot of a particular number
class Calculator:

    def __init__(self, n):
        self.n = n

    @staticmethod
    def Hello():
        print("Hello!")

    def square(self):
        print(f"The square of {self.n} is: {self.n*self.n}")

    def cube(self):
        print(f"The cube of {self.n} is: {self.n*self.n*self.n}")

    def square_Root(self):
        print(f"The square root of {self.n} is: {self.n**1/2}")


a = Calculator(4)
a.Hello()
a.square()
a.cube()
a.square_Root()