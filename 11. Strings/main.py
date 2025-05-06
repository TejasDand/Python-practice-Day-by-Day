name = "Tejas"
friend = "Aayush"
anotherFriend = "Rohanwar"
print("Hello, " + name)


#If we want to put double quotes again in the string, we can use outer part as a single quote
apple = 'He said, "I want to eat an apple".\n'
print(apple)


#Multi-line string
poem = '''You will need to state the reason for your visit.
Don’t say because I want to walk down old roads
and caress stone walls the color of my skin.
 
You will need to state the reason for your visit.
Don’t say because the olives are ready for harvest
and I will coax the fruit from the trees,
press it into liquid gold.
 
You will need to state the reason for your visit.
Don’t say because my parents’ house
still sits empty on a bluff overlooking the sea,
the green shutters my grandfather had just painted
remain sealed shut
and the army listed the property’s owners
as absentees.'''

# print(poem)
# print(poem[5]) #Printing character by index


print("\nLets use a for loop:\n")
for character in name: #Printing characters of string by using a for loop
    print(character)