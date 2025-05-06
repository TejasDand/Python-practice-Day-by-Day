#One star (*) means tuple

def average(*number):
    sum=0
    for i in number:
        sum = sum + i
    return sum/len(number)

avr = average(4, 5, 6, 8, 9, 5, 6, 3, 8, 7)
print(avr)



# def names(*name):
#     print("Hello,",name[0],name[1],name[2])

# names("Tejas", "Aayush", "Rohanwar")