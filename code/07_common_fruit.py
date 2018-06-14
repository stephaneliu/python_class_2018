fruit_1f = open('data/fruit1.txt')
fruit_2f = open('data/fruit2.txt')

fruit_1 = set(fruit_1f.readlines())
fruit_2 = set(fruit_2f.readlines())

print(fruit_1 & fruit_2)

fruit_1f.close()
fruit_2f.close()
