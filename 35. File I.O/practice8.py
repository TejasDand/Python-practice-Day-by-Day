import os

# Making the copy of file

# Read the file
with open("this p8.txt") as f:
    content = f.read()

# Make the copy of read file
with open("copy_text p8.txt", "w") as w:
    w.write(content)
    

# If you want to remove the file from operating system "copy_text p8.txt" then use this:

# os.remove("copy_text p8.txt")