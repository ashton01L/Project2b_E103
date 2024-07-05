# Author: Ashton Lee
# Github User: ashton01L
# Date: 7/5/2024

# Description: Asks the user for an input of a temperature in degrees Celsius
# and converts it to degrees Fahrenheit, using the formula F = (9/5)C + 32

def celsius_2_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

while True:
    try:
        celsius = float(input("Please enter a Celsius temperature.\n"))
        fahrenheit = celsius_2_fahrenheit(celsius)
        print("The equivalent Fahrenheit temperature is:")
        print(f"{fahrenheit:.1f}")
        break
    except ValueError:
        print("Invalid input. Please enter a valid input.")