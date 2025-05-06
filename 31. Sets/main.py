#Sets in python: Sets are unordered collection of data items. Set items are separated by commas and enclosed within curly brackets {}. Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items.

s = {1, 2, 6, 2, 1}
print(s)

s = {"Carla", 19, True, 19, False, False}
print(s)

# if "Carla" in s:
#     print("Yes!")

for value in s:
    print(value)

# s = {}
# print(type(s))

s = set()
print(type(s))