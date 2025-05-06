# Matching the content of the file

with open("this p8.txt") as f:
    content1 = f.read()

with open("copy_text p8.txt") as f:
    content2 = f.read()

# Checking if the file content are same or not
if content1 == content2:
    print("Yes the content of both files are matching!")
else:
    print("No the content of both files are not matching!")