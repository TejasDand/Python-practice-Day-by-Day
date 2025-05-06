# Ask the user for their name and age. You have to add 10 to the age inside the f-string.
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))

print(f"In 10 years, {name} will be {age + 10} years old.")



# You have two lists. Using a for loop and f-string, print:
# Alice scored 85 marks.
# Bob scored 90 marks.
# Charlie scored 95 marks.

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

print("\n")
for name, score in zip(names, scores):
    print(f"{name} scored {score} marks.")