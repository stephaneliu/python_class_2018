from convert import *

unit_conversion = { 'c': c2f, 'f': f2c,
                    'km': km2mi, 'mi': mi2km,
                    'kg': kg2lb, 'lb': lb2kg, }

human_units = { 'c': ('celsius', 'farenheit'),
                'f': ('farenheit', 'celsius'),
                'km': ('kilometer', 'mile'),
                'mi': ('mile', 'kilometer'),
                'kg': ('kilogram', 'pound'),
                'lb': ('pound', 'kilogram')
                }
while True:
    value = input("Conversion equation: ")

    if value == '':
        continue
    elif value.find('q') >= 0:
        break
    else:
        amount, unit = value.split()
        print(amount, human_units[unit][0], "is", unit_conversion[unit](float(amount)), human_units[unit][1])
