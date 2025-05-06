class Animals:
    pass

class Pets(Animals):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print("Bokh rha hu!")

d = Dog()
d.bark()