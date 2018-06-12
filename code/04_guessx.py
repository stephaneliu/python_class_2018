
MINVAL = int(input("Provide a min value: "))
MAXVAL = int(input("Provide a max value: "))

while True:
    guess = int((MINVAL + MAXVAL) / 2)
    response = input("Is your number {} (y/h/l/q): ".format(guess))

    if(response == 'q'):
        break
    elif(response == 'y'):
        print("Whooop!")
        break
    elif(response == 'h'):
        MAXVAL = guess
    elif(response == 'l'):
        MINVAL = guess
    else:
        print("y - 'yes', h - 'high', l - 'low', q - 'quit'")
