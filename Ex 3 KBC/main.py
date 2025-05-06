#KBC in python

questions = [
    "\nWhat is the correct file extension for Python files?",
    "\nWhich keyword is used to create a function in Python?",
    "\nHow do you insert COMMENTS in Python code?",
    "\nWhat is the output of: print(2 + 3 * 5)?",
    "\nWhich data type is used to store True or False values?"
]

options = [
    ["A) .pt", "B) .pyt", "C) .py", "D) .python"],
    ["A) def", "B) func", "C) function", "D) define"],
    ["A) /* This is a comment */", "B) // This is a comment", "C) -- This is a comment", "D) # This is a comment"],
    ["A) 25", "B) 17", "C) 21", "D) 20"],
    ["A) int", "B) str", "C) bool", "D) float"]
]

answers = ['C', 'A', 'D', 'B', 'C']

print("\nKBC mein aapka swagat hain! Mera naam hai Amitabh Bachan, aapka kya naam hai?")
name = input().title()

print("Toh chaliye,",name,"khel shuru karte hai!")


def askQuestions(idx):
    print(questions[idx])

    for o in options[idx]:
        print(o)
    
    correct_Ans = input("Enter your answer: ").upper()

    if(correct_Ans == answers[idx]):
        print("✅ Your answer is correct!")
    else:
        print("Your answer is wrong! Correct answer is:",answers[idx])
        print("You're out of the game!")
        exit()

askQuestions(0)
askQuestions(1)
askQuestions(2)
askQuestions(3)
askQuestions(4)

print("\nAapke saare jawab shi hai! ✅")
print("Aap jeet chuke hai 7 Crore! 🎉")