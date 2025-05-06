#Converting Celcius to Fahrenheit:

def c_to_f(c):
    return (c * 9/5) + 32

cel = int(input("Enter a Celsius: "))
f = c_to_f(cel)

print(f"Celsius is {cel}°C and Fahrenheit is {round(f, 1)}°F.")