name = input("Enter your name: ").title()
country = input("Enter your country name: ").title()

string1 = f"My name is {name}, and I am from {country}."
print(string1)

price = 49.159991513
txt = f"For only {price:.2f}$"
print(txt)

sum = f"{2 + 30}"
print(sum)



#If we have to print variable names also in string:
# string1 = f"My name is {{name}}, and I am from {{country}}."
# print(string1)