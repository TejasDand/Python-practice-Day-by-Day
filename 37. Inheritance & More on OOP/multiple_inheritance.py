# This is called multiple inheritance. Here, Company_name and Employee_name classes are parent classes and Language class is child class. Language class takes two classes within Company_name and Employee_name classes.


class Company_name:     # parent class
    company = "Microsoft"

    def comp_name(self):
        print(f"\nEmployee company name is {self.company} and employee name is {self.name}.")


class Employee_name:    # parent class
    name = "Tejas"

    def emp_name(self):
        print(f"\nHis name is {self.name} and his salary is {self.salary}.")


class Language(Company_name, Employee_name):    # child class
    language = "python"

    def lang(self):
        print(f"\nHis favorite language is {self.language} and his salary is {self.salary}.\n")


harry = Language()
harry.salary = 120000

harry.comp_name()
harry.emp_name()
harry.lang()