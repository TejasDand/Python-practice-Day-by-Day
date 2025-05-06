#Extracting names by indexing character values
names = "Tejas, Aayush"
print(names[:5]) #Here, second digit is (n-1) = 5 (5-1) = index[4]"s"
print(names[7:11])


#Length Function
print(len(names))


#"in" function use:
if "Aayush" in names:
    print("yes")
else:
    print("no")