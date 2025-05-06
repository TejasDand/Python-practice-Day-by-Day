# Set of all students
all_students = {"Amit", "Neha", "Raj", "Priya", "Zara"}

# Students who gave Exam 1 and Exam 2
exam1 = {"Amit", "Neha"}
exam2 = {"Raj", "Neha", "Amit"}

# 🧠 Find students who didn't attend any exam
# Expected Output: {"Priya", "Zara"}

print(all_students.difference(exam1, exam2))



list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# 🧠 Remove common elements from both lists and print the final sets.
# Expected Output:
# set1 = {1, 2, 3}
# set2 = {7, 8, 9}

slist1 = set(list1)
slist2 = set(list2)

print(slist1.difference(slist2))
print(slist2.difference(slist1))