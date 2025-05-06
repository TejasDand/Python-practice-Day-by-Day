#Just like Fibonacci, but instead of sum of last 2 numbers, it’s the sum of last 3 numbers!
#t(0)=0
#t(1)=1
#t(2)=1
#t(n-1) + t(n-2) + t(n-3)

def tribonacci(n):
    if n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
    

for i in range(int(input("Enter a number: "))):
    print(tribonacci(i), end=" ")