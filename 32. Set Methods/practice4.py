#Taking 8 number inputs from the user and integrate into the set with help of add() method.

s = set()

for i in range(8):
    i = int(input("Enter a number: "))
    s.add(i)

print(s)