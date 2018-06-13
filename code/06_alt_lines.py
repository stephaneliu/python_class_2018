source_file = open('data/alt.txt')
a_file      = open('data/a.txt', 'w')
b_file      = open('data/b.txt', 'w')
no_match    = open('data/no_match.txt', 'w')

for source in source_file:
    if source.startswith('a'):
        a_file.write(source)
    elif source.startswith('b'):
        b_file.write(source)
    else:
        no_match.write(source)

source_file.close()
a_file.close()
b_file.close()
no_match.close()