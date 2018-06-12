import sys

try:
    input_celsius = sys.argv[1]
    celsius       = float(input_celsius)
    fahrenheit    = ((celsius * 9) / 5 ) + 32
    print(input_celsius + "\u00b0 C is " + str(fahrenheit) + "\u00b0 F.")

    input_celsius = sys.argv[2]
    celsius       = float(input_celsius)
    fahrenheit    = ((celsius * 9) / 5 ) + 32
    print(input_celsius + "\u00b0 C is " + str(fahrenheit) + "\u00b0 F.")

    input_celsius = sys.argv[3]
    celsius       = float(input_celsius)
    fahrenheit    = ((celsius * 9) / 5 ) + 32
    print(input_celsius + "\u00b0 C is " + str(fahrenheit) + "\u00b0 F.")

    input_celsius = sys.argv[4]
    celsius       = float(input_celsius)
    fahrenheit    = ((celsius * 9) / 5 ) + 32
    print(input_celsius + "\u00b0 C is " + str(fahrenheit) + "\u00b0 F.")
except ValueError:
    print("Bad number. Cannot continue.")
    exit(1)
