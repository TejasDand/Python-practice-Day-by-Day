# Using Format Function

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Enter phoneNo.: "))

s = "The name of the student is {}, his marks are {} and phone number is {}.".format(name, marks, phone)
print(s)