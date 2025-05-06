class Employee:

    salary = 320
    increment = 20

    # This Calculates the updated salary using the current increment.
    @property
    def salaryAfterIncrement(self):

        return (self.salary + self.salary * (self.increment/100))   
        # 320 + 320 * (20/100) =>  320 + 320 * 0.2 =>  320 + 64 =>  384

    
    # This Calculates the required increment % to reach a target salary.
    @salaryAfterIncrement.setter
    def salaryIncrement(self, salary):

        self.increment = ((salary/self.salary) - 1) * 100
        # ((390.6 / 320) - 1) *100 =>   (1.220625 - 1)*100 =>   0.220625*100 =>     22.0625


e = Employee()
print(e.salaryAfterIncrement)   # 384.0
e.salaryIncrement = 390.6
print(e.increment)