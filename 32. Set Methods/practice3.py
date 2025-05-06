# Students who won Math Prize
math_prize = {"Amit", "Neha", "Sita", "Raj"}

# Students who won Science Prize
science_prize = {"Neha", "Raj", "Zara", "Aman"}

# Students who won English Prize
english_prize = {"Raj", "Neha", "Amit", "Isha"}


uni = math_prize.union(science_prize, english_prize)
inter = math_prize.intersection(science_prize, english_prize)

res = uni.difference(inter)
print(res)