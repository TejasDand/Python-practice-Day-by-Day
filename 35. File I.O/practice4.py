with open("practice4.txt") as f:
    content = f.read()
    
content_New = content.replace("Donkey", "######")

with open("practice4.txt", "w") as w:
    print(w.write(content_New))