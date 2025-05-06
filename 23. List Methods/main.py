#Various List Methods

l = [1, 2, 4, 45, 39, 64, 23, 4, 4, 6, 8 ,9]


#append(): This method appends items to the end of the existing list.
# l.append(7)
# print(l)


#sort(): This method sorts the list in ascending order. The original list is updated
# l.sort()
# l.sort(reverse=True) #Gives sorting in reverse order
# print(l)

colors =  ["voilet", "indigo", "blue", "green"]
# colors.sort()
# print(colors)


#reverse(): This method reverses the order of the list. 
# l.reverse()
# print(l)


#index(): This method returns the index of the first occurrence of the list item.
# print(l.index(64))


#count(): Returns the count of the number of items with the given value.
# print(l.count(4))


#copy(): Returns copy of the list. This can be done to perform operations on the list without modifying the original list.
# newList = l.copy()
# newList[1] = 0
# print(l)
# print(newList)


#insert(): This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method.
# colors.insert(2, "red")
# print(colors)


#extend(): This method adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
lst = ["Legend", "Aayush", "Argha"]
# l.extend(lst)
# print(l)


#Concatenating two lists: You can simply concatenate two lists to join two lists.
# print(l + lst)


#min(): This function returns the smallest item in an iterable or the smallest among two or more arguments.
# smallestString = min(colors, key=len)
# print(smallestString)


#max(): This function returns the largest item in an iterable or the largest among two or more arguments.
# largestString = max(colors, key=len)
# print(largestString)