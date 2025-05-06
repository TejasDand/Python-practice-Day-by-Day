# Making Calculator to find the square, cube and squareRoot of a particular number

class Calculator:

    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is: {self.n*self.n}")

    def cube(self):
        print(f"The cube is: {self.n*self.n*self.n}")

    def square_Root(self):
        print(f"The square root is: {self.n**1/2}")


a = Calculator(int(input("Enter a number: ")))
a.square()
a.cube()
a.square_Root()