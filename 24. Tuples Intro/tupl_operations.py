#Manipulating Tuples:
country = ("India", "Russia", "USA", "France", "Japan", "Dubai", "China")
temp = list(country) #Converting Tuple to List

#Manipulating List
temp.append("South Korea")
temp.pop(6)
temp.insert(6, "Nepal")
temp.sort()

country = tuple(temp) #Converting List to Tuple
print(country)



#Concatenating two Tuples:
country2 = ("Thailand", "Germany", "New Zealand")
print(country + country2)



#count() method:
numl = (1, 1, 2, 3, 2, 6, 3, 1)
print(numl.count(1))

#index() method:
print(numl.index(6))