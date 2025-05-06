# This is called multilevel inheritance. Here, Employee is parent class and Programmer is child class and it inherit the employee class and Manager is also child class but it inherit the programmer class.


class Employee:     # parent class
    name = "Tejas"

    def emp(self):
        print(f"\nEmployee name is {self.name} and programmer name is {self.pname}.")

class Programmer(Employee):     # child 1 class
    pname = "Aayush"

    def prog_name(self):
        print(f"\nProgrammer name is {self.pname} and Manager name is {self.mname}.")
    
class Manager(Programmer):      # child 2 class
    mname = "Rohan"

    def manag_name(self):
        print(f"\nManager name is {self.mname} and he give workload to both employee - {self.name} and programmer - {self.pname}.\n")


names = Manager()
names.emp()
names.prog_name()
names.manag_name()