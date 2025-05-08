myList = [1, 2, 3, 4, 5, 6]

# Without using List Comprehension:
# cubeList = []

# for i in myList:
#     cubeList.append(i*i*i)

# print(cubeList)



# Using List Comprehension:
cubeList = [i*i*i for i in myList]
print(cubeList)