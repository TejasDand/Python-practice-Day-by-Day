info = {'name': 'Tejas', 'age': 18, 'isStudent': True, 'address': 'Mundra'}
# print(info['name'])
# print(info.get('address')) #This get() method don't give error, it returns only 'none' type.


#key() & value(): To access all keys and values.
# print(info.keys())
# print(info.values())


#Using for loop to access or print values and keys:
# for key in info.keys():
    # print(info[key])
    # print(f"The value of corresponding to the key {key} is {info[key]}.")



#items() method: This method prints all keys with corresponding values.
# print(info.items())


#Using for with items() method:
for key, value in info.items():
    # print(key,":",value)
    print(f"The value of corresponding to the key {key} is {value}.")