# Finding lenght of Vector:

class Vector:

    def __init__(self, l):
        self.l = l

    def __len__(self):
        return len(self.l)
    
v = Vector([1, 2, 3, 4, 5, 6])
print(len(v))