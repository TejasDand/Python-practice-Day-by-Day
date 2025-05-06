#Taking 4 friends input as a name and their favorite programming language

d = {}

for i in range(4):
    i = name = (input("Enter your name: ")).title()
    i = lang = input("Enter your favorite language name: ").title()
    d.update({name:lang})

print(d)