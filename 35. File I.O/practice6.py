with open("practice6.txt") as f:
    content = f.read()

if "python" in content:
    print("Yes, python word is present!")
else:
    print("No, python word is not present!")