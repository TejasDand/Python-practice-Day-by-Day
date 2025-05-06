countries1 = {"India", "USA", "Russia", "France", "Iran"}
countries2 = {"France", "Iran"}

#SET METHODS:

#isdisjoint(): This method checks if items of given set are present in another set. This method returns False if items are present, else it returns True.
# print(countries1.isdisjoint(countries2))


#issuperset(): This method checks if all the items of a particular set are present in the original set. It returns True if all the items are present, else it returns False.
# print(countries1.issuperset(countries2))


#issubset(): This method checks if all the items of the original set are present in the particular set. It returns True if all the items are present, else it returns False.
# print(countries2.issubset(countries1))


#add(): If you want to add a single item to the set use the add() method.
# countries1.add("Argentina")
# print(countries1)


#update(): If you want to add more than one item, simply create another set or any other iterable object(list, tuple, dictionary), and use the update() method to add it into the existing set.
# countries3 = {"West Indies", "Australia", "South Africa"}

# countries1.update(countries3)
# print(countries1)


#remove() & discard(): We can use remove() and discard() methods to remove items form list. The main difference between remove and discard is that, if we try to delete an item which is not present in set, then remove() raises an error, whereas discard() does not raise any error.

# countries1.discard("Iran")
# print(countries1)

# countries1.remove("USA")
# print(countries1)


#pop(): This method removes the last item of the set but the catch is that we don’t know which item gets popped as sets are unordered. However, you can access the popped item if you assign the pop() method to a variable.

# item = countries1.pop()
# print(countries1)
# print(item)


#del: del is not a method, rather it is a keyword which deletes the set entirely.
# del countries2
# print(countries2)


#clear(): This method clears all items in the set and prints an empty set.
countries2.clear()
print(countries2)