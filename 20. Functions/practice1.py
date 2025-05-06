#Finding table values using function
def tableF(table):

    for i in range(1, 11):
        print(f"{table} x {i} = {table*i}")

tableF(table = int(input("Enter a number: ")))