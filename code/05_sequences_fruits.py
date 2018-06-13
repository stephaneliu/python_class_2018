fruits = [
    '      MANGO', 'Apple', '   peach   ',
    'PLUM   ', '   Apricot', 'BaNaNa', 'Persimmon'
    ]

clean_fruits = [ fruit.strip().lower() for fruit in fruits ]

print(clean_fruits)
