#Count Word Frequency:

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)



#Highest Scorer:

scores = {"Amit": 75, "Neha": 88, "Raj": 82, "Zara": 91}
highest = max(scores, key=scores.get)

print(f"Topper is {highest} with {scores[highest]} marks.")



#Filter Students Passed:

students = {"Amit": 35, "Neha": 52, "Raj": 29, "Zara": 60}
passed = {}

for name, marks in students.items():
    if marks>=40:
        passed[name] = marks

print(passed)