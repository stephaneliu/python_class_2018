while True:
    input_celsius = input("Provide celsius temperature: ")

    if input_celsius == "q":
        break
    try:
        celsius       = float(input_celsius)
    except ValueError:
        print("Bad number. Cannot continue.")
        exit(1)

    fahrenheit    = ((celsius * 9) / 5 ) + 32
    print(input_celsius + "\u00b0 C is " + str(fahrenheit) + "\u00b0 F.")
