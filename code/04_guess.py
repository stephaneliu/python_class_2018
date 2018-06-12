MINVAL = 0
MAXVAL = 26

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
    else:
        MINVAL = guess
