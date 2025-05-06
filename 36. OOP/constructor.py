class Employee:
    # name = "Harry"       
    language = "Python"  
    salary = 1200000

    def __init__(self, name, language, salary):     # Dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
        print("Good Morning!")


harry = Employee("Harry", "Javascript", 120000)
print(harry.name, harry.language, harry.salary)

rohan = Employee("Rohan", "C++", 1561256)
print(rohan.name, rohan.language, rohan.salary)