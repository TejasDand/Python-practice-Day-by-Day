#Skipping all odd numbers from 1 to 20

for i in range(1, 51):
    if(i%2!=0):
        continue
    print(i)