# Censor the words in practice4.txt file

censor_W = ["Donkey", "ganda", "bad"]   # Pahle censor words ki ek list banayi

with open("practice4.txt") as f:    # Phir file ko read kiya
    content = f.read()  

for word in censor_W:
    content = content.replace(word, "*" * len(word))    # Or ek loop "word" name ka chalaya, woh list ke words ko lega, phir humne word ko replace karke length of word ko lekar, "*" print kar diya.

with open("practice4.txt", "w") as w:   # Phir file ko write kar diya
    w.write(content)    