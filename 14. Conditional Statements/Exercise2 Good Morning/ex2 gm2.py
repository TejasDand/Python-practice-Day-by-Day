#Write a program to greet the sir according to time zone of India (Solution-2)
import time

name = input("Enter your name: ").capitalize()
recentTime = time.strftime("%H:%M")
print("Current time is:",recentTime)

hr = int(time.strftime("%H"))

if(hr>=5 and hr<12):
    print("Good Morning",name,"sir!")

elif(hr>=12 and hr<17):
    print("Good Afternoon",name,"sir!")

elif(hr>=17 and hr<21):
    print("Good Evening",name,"sir!")

else:
    print("Good Night",name,"sir!")