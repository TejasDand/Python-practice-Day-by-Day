# It is shortest and suitable way to open the file and here we don't want to close this file in this statement.

st = input("Enter your name: ")

with open("more_Lines.txt", "a") as c:   
    c.write(st)