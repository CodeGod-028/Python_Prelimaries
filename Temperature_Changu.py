'''Temperature Converter
Objective: Convert temperatures between Celsius, Fahrenheit, and Kelvin.
Features: Ensures valid input and supports multiple conversions in one session.'''

def temperature_converter():    
    while True:
        try:
            choice = int(input("Enter 1 to convert Celsius to Fahrenheit, 2 to convert Celsius to Kelvin, 3 to convert Fahrenheit to Celsius, 4 to convert Fahrenheit to Kelvin, 5 to convert Kelvin to Celsius, 6 to convert Kelvin to Fahrenheit: "))
            if choice < 1 or choice > 6:
                print("Invalid choice. Please enter a number between 1 and 6.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
    
    while True:
        try:
            temperature = float(input("Enter the temperature: "))
            if choice == 1:
                result = (temperature * 9/5) + 32
                print(f"{temperature}°C is equal to {result}°F.")
            elif choice == 2:
                result = temperature + 273.15
                print(f"{temperature}°C is equal to {result}°K.")
            elif choice == 3:
                result = (temperature - 32) * 5/9
                print(f"{temperature}°F is equal to {result}°C.")
            elif choice == 4:
                result = (temperature - 32) * 5/9 + 273.15
                print(f"{temperature}°F is equal to {result}°K.")
            elif choice == 5:
                result = temperature - 273.15
                print(f"{temperature}°K is equal to {result}°C.")
            elif choice == 6:
                result = (temperature - 273.15) * 9/5 + 32
                print(f"{temperature}°K is equal to {result}°F.")
            break
        except ValueError:
            print("Invalid input. Please enter a valid temperature.")

    while True:
        choice = input("Do you want to convert another temperature? (y/n): ")
        if choice.lower() == "y":
            temperature_converter()
        elif choice.lower() == "n":
            print("Thank you for using the temperature converter.")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

temperature_converter() # Call the function to start the program    