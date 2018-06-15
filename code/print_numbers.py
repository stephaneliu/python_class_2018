import re

file = open('data/custinfo.dat')

pattern = re.compile(r"^(\d{3}-)?\d{3}-\d{4}$")


for line in file:
    if pattern.search(line):
        print(line[:-1])

file.close()