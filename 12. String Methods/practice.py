fruit = "apple"
print(len(fruit))


#Automatic Slicing:
print(fruit[:4]) #When first digit not declares, python automatically put index[0]
print(fruit[2:]) #When second digit not declares, python automatically put length of string. Here, length of "apple" is 5.


#Slicing:
print(fruit[2:4])
print(fruit[1:4])


#Negative Slicing:
print(fruit[:-3]) #length of apple = 5. So, 5-3 = 2, 2 is second digit, so (n-1 = 2-1 = 1). So, 5-3 = index[1]. So, index[0] to index[1], Answer is: "ap"

print(fruit[-4:-2]) #length of apple = 5. So, 5-4 = index[1] and 5-2 = 3, 3 is second digit, so (n-1 = 3-1 = 2). So, 5-2 = index[2]. Answer is: "pp"

print(fruit[-5:-2])


#Quick Quiz:
nm = "Harry"
print(nm[-4:-2]) #5-4=1, 5-2=3 (n-1 = 3-1 = 2), index[1] to index[2]. Answer: "ar"