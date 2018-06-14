def c2f(input_celsius):
    try:
        celsius       = float(input_celsius)
        fahrenheit    = ((celsius * 9) / 5 ) + 32
        return fahrenheit
    except ValueError:
        print("Bad number. Cannot continue.")
        exit(1)

celsius_temps = [100, 0, 37, -40]

for celsius in celsius_temps:
    fahrenheit = c2f(celsius)
    print(str(celsius) + "\u00b0 C is " + str(fahrenheit) + "\u00b0 F.")
