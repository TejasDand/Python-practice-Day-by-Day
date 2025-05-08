# Printing 3, 6, 8 element using enumerate function

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i, item in enumerate(l):
    if i == 3 or i == 6 or i == 8:
        print(item)