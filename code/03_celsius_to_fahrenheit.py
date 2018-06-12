import sys

input_celsius = input("Provide celsius temperature: ")
celsius = float(input_celsius)
fahrenheit = ((celsius * 9) / 5 ) + 32
print(input_celsius + "\u00b0 C is " + str(fahrenheit) + " \u00b0F.")
