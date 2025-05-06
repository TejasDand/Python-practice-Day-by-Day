tupl = ("Green", "Red", "Blue", "Orange", "Argha", "Aayush", "Legend")

# print(tupl)
# print(tupl[3])
# print(tupl[:5])
# print(tupl[3:6])
# print(tupl[1:-3])
# print(tupl[2:-1:2])
# print(tupl[::3])

for i in tupl:
    print(i)

newTupl = [j for j in tupl if len(j)%2==0]
print(newTupl)

newTupl = [k for k in tupl if len(k)>4]
print(newTupl)

if "Green" in tupl:
    print("YES")