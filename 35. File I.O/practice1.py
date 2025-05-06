with open("practice1.txt") as f:
    r = f.read()

    if "Twinkle" in r:
        print("Yes, it is present in the content.")
    else:
        print("No, it is not present in the content.")