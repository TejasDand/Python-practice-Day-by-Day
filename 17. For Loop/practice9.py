# Printing reverse table:

table = int(input("Enter a number for table: "))

#Using for loop:
for i in range(1, 11):
    print(f"{table} x {11 - i} = {table * (11 - i)}")



#Using while loop:
# i = 10

# while(i>=1):
#     print(f"{table} x {i} = {table*i}")
#     i-=1