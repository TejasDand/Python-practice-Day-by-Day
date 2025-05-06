#String Methods Part-2:

#Index() - This method searches for the first occurrence of the given value and returns the index where it is present. If given value is absent from the string then raise an exception.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.index("Dan"))

#Isalnum() - This method returns True only if the entire string only consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.
str1 = "WelcomeToTheConsole00"
print(str1.isalnum())

#Isalpha() - This method returns True only if the entire string only consists of A-Z, a-z. If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(str1.isalpha())

#Islower() - This method returns True if all the characters in the string are lower case, else it returns False.
str2 = "hello  world"
print(str2.islower())

#Isupper() - This method returns True if all the characters in the string are upper case, else it returns False.
print(str2.isupper())

#Isprintable() - This method returns True if all the values within the given string are printable, if not, then return False.
str3 = "Welcome!\n"
print(str3.isprintable())

#Isspace() - This method returns True only and only if the string contains white spaces, else returns False.
str3 = "    "
print(str3.isspace())

#Istitle() - This returns True only if the first letter of each word of the string is capitalized, else it returns False.
str3 = "World Health Organization"
print(str3.istitle())

#Startswith() - This method checks if the string starts with a given value. If yes then return True, else return False.
print(str3.startswith("World"))

#Swapcase() - This method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.
print(str3.swapcase())

#title() - This method capitalizes each letter of the word within the string.
str3 = "last lesson"
print(str3.title())