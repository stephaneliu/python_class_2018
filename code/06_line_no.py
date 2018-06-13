import sys

for file_name in sys.argv[1:]:
    with open(file_name) as file:
        count = 1
        for line in file:
            print(count, line.rstrip())
            count += 1
