"""
write a program which prompts the user for a celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.
Formula: (C*9/5)+32 = F
"""
celsius = int(input("Enter Temperature in celsius: \n"))

fahrenheit = (celsius * 9/5) + 32

# print(type(celsius))

print(f"{celsius} Celsius is = to {fahrenheit} Fahrenheit")