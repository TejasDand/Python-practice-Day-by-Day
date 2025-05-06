lst2 = ["Aayush", "Tejas", "Rohanwar", "Jay", 4, 5, 9, 135]


#"in" function use:
# if 135 in lst2:
#     print("Yes")
# else:
#     print("No")


#Lists comprehension:
# lst3 = [i for i in range(10)]
# print(lst3)

# lst3 = [i*i for i in range(10)]
# print(lst3)

# lst3 = [i for i in range(20) if i%2==0]
# print(lst3)

names = ["Aayush", "Rohanwar", "Argha", "Jay", "Ritik", "Sahil", "Legend"]
namesWith_ = [j for j in names if "l" in j]
print(namesWith_)

namesWith_ = [k for k in names if len(k)>5] #print names, in which names have greater than 5 characters
print(namesWith_)

namesWith_ = [e for e in names if len(e)%2!=0] #print names, in which names have only odd number characters
print(namesWith_)