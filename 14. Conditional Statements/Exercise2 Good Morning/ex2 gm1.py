#Write a program to greet the sir according to time zone of India (Solution-1)

name = input("Enter your name: ").title()
hr = int(input("Enter your recent time hour: "))

if(hr>=5 and hr<12):
    print("Good Morning",name,"sir!")

elif(hr>=12 and hr<17):
    print("Good Afternoon",name,"sir!")

elif(hr>=17 and hr<21):
    print("Good Evening",name,"sir!")

else:
    if(hr>=21 and hr<=24):
        print("Good Night",name,"sir!")
    elif(hr>=1 and hr<5):
        print("Good Night",name,"sir!")
    else:
        print("Enter a valid time in 24-hour format...")