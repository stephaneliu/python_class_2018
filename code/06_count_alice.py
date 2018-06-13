file_name = 'data/alice.txt'

with open(file_name) as alice_file:
    alice_count = 0
    for line in alice_file:
       if 'Alice' in line:
           alice_count += 1

print(file_name, "has", alice_count, "instances of 'Alice'")
