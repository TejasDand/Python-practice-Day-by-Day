# Simple example of Class

class Employee:
    # name = "Harry"       
    language = "Python"     # This is a class attribute
    salary = 1200000

harry = Employee()
harry.name = "Harry"    # This is a instance attribute
print(harry.name, harry.language, harry.salary)


rohan = Employee()
rohan.name = "Rohan Roro Akitson"
print(rohan.name, rohan.salary, rohan.language)


aayush = Employee()
aayush.language = "C++"
aayush.salary = 12000       # Instance (object) attributes, take preference over class attributes during assignment & retrieval
print(aayush.language, aayush.salary)


# Here name and language is a class attribute as they directly belong to the class and name is a instance attribute