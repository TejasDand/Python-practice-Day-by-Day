# Identify karo konse line mein python word aaya hai "practice6.txt" wali file mein

with open("practice6.txt") as f:    # Pahle saari practice6.txt wali mein, saari lines ko read kar liya
    lines = f.readlines()

lineno = 1    

for line in lines:
    if "python" in line:
        print(f"Yes, python is present. Line no. is {lineno}")  # Agar "python" word mil jaye toh line number daalke break kar do
        break
    lineno += 1 # Nhi toh phir line ko badhate raho

else:
    print("No, python word is not present")     # Agar word hi naa ho pure file mein, toh else print kardo