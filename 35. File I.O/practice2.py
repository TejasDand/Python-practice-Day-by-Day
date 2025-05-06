# Ye program baar baar hiscore update karega 1 se 62 ke beech mein. Or ye update hiscore.txt wali file mein hoga. 

import random

def game():
    print ("You're playing a game...")

    score = random.randint(1, 62)   # Random number lega 1 se 62 ke beech mein

    with open("hiscore p2.txt") as f:  # hiscore.txt wali file open karega read karne ke liye
        hiscore = f.read() 

        if (hiscore != ""):     # Agar hiscore ki file mein space nhi hai toh hiscore daal do as a int.
            hiscore = int(hiscore)
        else:       # Agar hiscore ki file mein space ho toh hiscore 0 kardo.
            hiscore = 0
    
    print(f"Your score is {score}")

    if(score>hiscore):      # Agar random number (score) bada ho hiscore se toh score ko write kardo file mein

        with open("hiscore p2.txt", "w") as w:     # Score write kar rhe hai, hiscore wali file mein as a string 
            w.write(str(score))
    
    return score

game()