a = int(input("Enter Value of A: "))
b = int(input("Enter Value of B: "))
c = int(input("Enter Value of C: "))

if(a>b and a>c):
    print("A is Max:", a)

elif(b>c and b>a):
    print("B is Max:", b)

else:
    print("C is Max:", c)