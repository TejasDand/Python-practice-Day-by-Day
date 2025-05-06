#Printing only even number table till 20 using for loop with range using 3 parameters.
table = int(input("Enter a number for table: "))

for i in range(2, 21, 2):
    print(table,"x",i,"=",table*i)