import re

file = open("data/eggs.txt")
buffer = file.read()
pattern = re.compile(r"You")

print(pattern.findall(buffer))
print()

def downcase(m):
    return m.group(0).lower()

matches, count = pattern.subn(downcase, buffer)

print("--------------------")
print(matches)
print(count, "occurences")

file.close()