#Printing only even numbers.

#Solution-1:
# given_range = int(input("Enter a given range number: ")) #like 1 - 10, 15, 20, etc...

# for i in range(2, given_range+1, 2):
#     print(i)



#Solution-2:
given_range = int(input("Enter a given range number: ")) #like 1 - 10, 15, 20, etc...

for i in range(given_range+1):
    if i%2==0:
        print(i)