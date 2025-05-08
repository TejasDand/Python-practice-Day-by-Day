# Else, try-except block mein tab chalega jab try block execute hoga.

try:
    a = int(input("Enter a number: "))

except Exception as e:
    print(e)

else:       # Agar try - except block mein error hoga toh ye part execute nhi hoga.
    print("Try block successfully execute hua, isliye mein bhi ho gya!")