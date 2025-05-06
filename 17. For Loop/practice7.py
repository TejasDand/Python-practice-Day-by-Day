#Checking whether given number from user is Prime or Not.

prime_N = int(input("Enter a Number: "))

for is_prime in range(2, prime_N): 

    if(prime_N % is_prime == 0):
        print("Number is not prime!")
        break

else:
    print("Number is Prime!")