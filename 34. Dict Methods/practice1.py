# You are given a dictionary of subject marks:
# Add a new subject "Computer" with marks 95, and then print the updated dictionary.

marks = {
    "Math": 90,
    "Science": 85,
    "English": 88
}
new_Subject = {"Computer": 95}

marks.update(new_Subject)
print(marks)



# Check if the key "age" exists in the dictionary.
# If yes, print "Age is present", else "Age not found".

student = {
    "name": "Amit",
    "age": 17,
    "grade": "A"
}

if "age" in student:
    print("Age is present!")
else:
    print("Age not found!")



# Print each fruit and its quantity like this:
# "We have 3 apples", "We have 5 bananas", etc.

fruits = {
    "apple": 3,
    "banana": 5,
    "mango": 2
}

for key, value in fruits.items():
    print(f"We have {value} {key}s.")