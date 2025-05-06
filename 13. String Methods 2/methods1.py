#Strings are immutable.

#String Methods Part-1:
a = "Tejas..."

#Length() - Gives length of the string.
print(len(a))

#UpperCase() - Converts string into uppercase.
print(a.upper())

#LowerCase() - Converts string into lowercase.
print(a.lower()) 

#Strip() - Removes any white spaces before and after the string.
b = "Legend Bada Bhai "
print(b.strip())

#rStrip() - Removes any trailing characters.
print(a.rstrip("."))

#Replace() - Replaces all occurences of a string with another string.
print(b.replace("Legend", "Aayush"))

#Split() - Splits the given string at the specified instance and returns the separated string as list items.
print(b.split(" "))

#Capitalize() - This method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase. The string has no effect if the first character is already uppercase.
c = "introduction To pYthON"
print(c.capitalize())

#Center() - This method aligns the string to the center as per the parameters given by the user.
print(b.center(50, "."))

#Count() - This method returns the number of times the given value has occurred within the given string.
print(b.count("a"))

#Endswith() - This method checks if the string ends with a given value. If yes then return True, else return False.
d = "Welcome"
print(d.endswith("e"))

d = "Welcome in the world of Python. Welcome...."
print(d.endswith("in", 3, 10))

#Find() - This method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then return -1.
print(d.find("in"))