'''
Celsius to Fahrenheit: F = (C * 9/5) + 32; 
Celsius to Kelvin: K = C + 273.15; 
Fahrenheit to Celsius: C = (F - 32) * 5/9; 
Fahrenheit to Kelvin: K = (F - 32) * 5/9 + 273.15; 
Kelvin to Celsius: C = K - 273.15; 
Kelvin to Fahrenheit: F = (K - 273.15) * 9/5 + 32.

'''


# Temperature Calculator Function:

def temperature_Calc():

    print("\nWelcome to the Temperature Converter!")
    print("\nC = Celsius, F = Fahrenheit, K = Kelvin\n")

    inpt = input("Choose the input unit (C/F/K): ").upper()
    oupt = input("Choose the output unit (C/F/K): ").upper()


    # Celsius to Farenheit
    if(inpt == "C" and oupt == "F"):
        temperature = int(input("\nEnter temperature value: "))

        f = (temperature * 9/5) + 32
        print(f"\nFahrenheit: {round(f, 2)}°F 🔥")


    # Celsius to Kelvin
    elif(inpt == "C" and oupt == "K"):
        temperature = int(input("\nEnter temperature value: "))

        k = temperature + 273.15
        print(f"\nKelvin: {round(k, 2)} K 🧪")


    # Fahrenheit to Celsius 
    elif(inpt == "F" and oupt == "C"):
        temperature = int(input("\nEnter temperature value: "))

        c = (temperature - 32) * 5/9
        print(f"\nCelsius: {round(c, 2)}°C 🧊")


    # Fahrenheit to Kelvin
    elif(inpt == "F" and oupt == "K"):
        temperature = int(input("\nEnter temperature value: "))

        k = (temperature - 32) * 5/9 + 273.15
        print(f"\nKelvin: {round(k, 2)} K 🧪")


    # Kelvin to Celsius
    elif(inpt == "K" and oupt == "C"):
        temperature = int(input("\nEnter temperature value: "))

        c = temperature - 273.15
        print(f"\nCelsius: {round(c, 2)}°C 🧊")


    # Kelvin to Fahrenheit
    elif(inpt == "K" and oupt == "F"):
        temperature = int(input("\nEnter temperature value: "))

        f = (temperature - 273.15) * 9/5 + 32
        print(f"\nFahrenheit: {round(f, 2)}°F 🔥")


    # If input and output is invalid
    else:
        print("\nInvalid input. Please enter C, F, or K!")

temperature_Calc()

# Last Thankyou Statement
print("\nThankyou! 🙏 for using my Temperature Calculator. 🌡️\n")