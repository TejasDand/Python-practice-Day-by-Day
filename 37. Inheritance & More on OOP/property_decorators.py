class Employee:

    @property
    def name(self):
        # This method acts like an attribute due to @property
        # It returns the full name by combining fname and lname
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        # This is the setter for the 'name' property
        # When you assign to 'e.name', this code runs
        # It splits the full name into first and last name
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

# Create an object of Employee class
e = Employee()

# Set the full name using the setter
e.name = "Harry Khan"  # Internally runs name.setter()

# Get the full name using the getter
print(e.name)  # Internally runs name() decorated with @property

# Call the class method to show class attribute value
e.show()