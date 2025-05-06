class Employee:
    # name = "Harry"       
    language = "Python"  
    salary = 1200000

    def getInfo(self):
        print(f"Employee name is {self.name} and his favorite language is {self.language} and his salary is {self.salary}")
    
    @staticmethod       # This method defines, the function didn't need any object property.
    def greet():
        print("Good Morning!")


harry = Employee()
harry.name = "Harry"    # added new instance attribute 'name'
harry.language = "JavaScript"   # update language 

harry.greet()
harry.getInfo()     # This arguement call looks like this - Employee.getInfo(harry)