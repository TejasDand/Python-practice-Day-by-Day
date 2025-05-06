# Iss program mein hum mein ek folder bnana hai jis mein 1 se leke 20 tak ki table ho.

def generate_Table(n):
    table = ""     # table ko humne khali string di hai

    for i in range(1, 11):
        table += f"{n} x {i} = {n*i}\n"     # phir humne table ko f string se plus kar diya hai, kyunki agar file mein write karna hai toh uska string hona jaruri hai.

    with open(f"tables/table_{n}.txt", "w") as f:   # phir humne tables ka ek folder banaya or us mein table karke ek .txt file banaya or uske name mein "n" ka parameter diya hai.
        f.write(table)
    

for i in range(2, 21):
    generate_Table(i)   # Idhar humne loop chalaya 2 se leke 20 tak or phir uss loop ke under function ko call kiya or "i" as a parameter (n) ki jagah dal diya.