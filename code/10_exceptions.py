while True:
    file_name = input("File to parse: ")

    if file_name == 'q':
        break

    try:
        file = open(file_name)
    except IOError as err:
        print("File could not be found. Try again.")
        continue

    for index, line in enumerate(file, 1):
        try:
            fl_1, fl_2 = [ float(num) for num in line.split()]
            print("Division of two", fl_1 / fl_2)
        except ZeroDivisionError:
            print("Line", index, "with values '", line.rstrip(), "' has division by zero error")
        except Exception:
            print("Line", index, "with values '", line.rstrip(), "' could not be parsed correctly")


