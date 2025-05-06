#Converting inch to cm:

def inch_to_cm(inch):
    return inch * 2.54

inch = int(input("Enter inches: "))
cms = inch_to_cm(inch)

print(f"Inch is {inch} and Centimeter is {round(cms, 2)}")