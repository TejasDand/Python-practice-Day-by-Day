color1 = {"Red", "Green", "Blue", "Yellow", "Orange"}
color2 = ("Blue", "Green", "Indigo", "White")

#JOINING SETS METHODS:

#The union() and update() methods prints all items that are present in the two sets:

#union(): The union() method returns a new set.
# print(color1.union(color2))

#update(): The update() method adds item into the existing set from another set.
# color1.update(color2)
# print(color1)
# print(color2)



#The intersection() and intersection_update() methods prints only items that are similar to both the sets:

#intersection(): The intersection() method returns a new set.
# print(color1.intersection(color2))

#intersection_update(): This method updates into the existing set from another set.
# color1.intersection_update(color2)
# print(color1)
# print(color2)



#The symmetric_difference() and symmetric_difference_update() methods prints only items that are not similar to both the sets:

#symmetric_difference(): This method returns a new set.
# print(color1.symmetric_difference(color2)) 

#symmetric_difference_update(): This method updates into the existing set from another set.
# color1.symmetric_difference_update(color2)
# print(color1)
# print(color2)



#The difference() and difference_update() methods prints only items that are only present in the original set and not in both the sets:

#difference(): This method returns a new set.
print(color1.difference(color2))

#difference_update(): This method updates into the existing set from another set.
color1.difference_update(color2)
print(color1)
print(color2)