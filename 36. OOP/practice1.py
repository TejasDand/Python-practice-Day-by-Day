# Employees working in Microsoft and add some details about the employess using the class Programmer.

class Programmer:
    company = "Microsoft"

    def __init__(self, name, salary, pinCode):
        self.name = name
        self.salary = salary
        self.pinCode = pinCode


t = Programmer("Tejas", 1250000, 370456)
print(t.company, t.name, t.salary, t.pinCode)

a = Programmer("Aayush", 1400000, 370984)
print(a.company, a.name, a.salary, a.pinCode)