class twoD_Vector:

    def __init__(self, i, j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The 2D vector is {self.i}i + {self.j}j")


class threeD_Vector(twoD_Vector):

    def __init__(self, i ,j , k):
        super().__init__(i, j)
        self.k = k
    
    def show(self):
        print(f"The 3D vector is {self.i}i + {self.j}j + {self.k}k")


a = twoD_Vector(5, 6)
a.show()

b = threeD_Vector(7, 8, 9)
b.show()