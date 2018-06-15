import re

while True:
    args = input("'pattern' file_name... ")

    if(args[0] == 'q'):
        print("Goodbye")
        break

    pattern = args.split()[0]
    file_names = args.split()[1:]
    regex = re.compile(pattern)

    for file_name in file_names:
        file = open(file_name)

        print("File:", file_name)

        for index, line in enumerate(file, 1):
            for match in regex.finditer(line):
                print("Found match on line", index, "in:", line)
        file.close

