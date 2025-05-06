# super keyword use...

class Employee_name:    # parent class

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

        print("\nIt prints the employee name and salary.")


class Employee_age(Employee_name):  # child class

    def __init__(self, name, salary, age):

        super().__init__(name, salary)  # super().__init__(...) allows the child class to call the parent’s constructor, so it can reuse the logic written there (instead of repeating it).

        self.age = age

        print("\nIt prints only employee age.\n")


tejas = Employee_age("Tejas", 125600, 18)

print(f"{tejas.name}, {tejas.salary}, {tejas.age}.\n")