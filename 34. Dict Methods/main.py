info1 = {'name':'Tejas', 'age':18, 'stdc':455, 'address':'Mundra'}
info2 = {'name':'Aayush', 'age':20, 'stdc':457, 'address':'Vadodara'}

new_Data = {'isStudent':'True'}

#Dict methods: Same as list, tuple and sets.

#update(): The update() method updates the value of the key provided to it if the item already exists in the dictionary, else it creates a new key-value pair.
# info1.update(new_Data)
# print(info1)

# info1.update(info2)
# print(info1)


#clear(): The clear() method removes all the items from the list.
# info2.clear()
# print(info2)


#pop(): The pop() method removes the key-value pair whose key is passed as a parameter.
# info2.pop('age')
# print(info2)


#popitem(): The popitem() method removes the last key-value pair from the dictionary.
# info1.popitem()
# print(info1)


#del: we can also use the del keyword to remove a dictionary item.
del info2['stdc']
print(info2)