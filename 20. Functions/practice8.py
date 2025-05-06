# Write a function to remove a word from a list and strip it at the same time.

l = ["Tejas", "Aayush", "Jay", "as"]

def rem(l, word):
    n = [] 

    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

print(rem(l, "as"))