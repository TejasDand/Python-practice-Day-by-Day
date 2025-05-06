#Write a program to calculate how much road tax should paid on the basis of cost price of a bike.

cp = int(input("Enter a cost price of a bike: "))

if(cp<=50000):
    print("According to the cost price, you will have to pay this much road tax:", cp*5/100)

elif(cp>50000 and cp<=100000):
    print("According to the cost price, you will have to pay this much road tax.", cp*10/100)

else:
    print("According to the cost price, you will have to pay this much road tax.", cp*15/100)