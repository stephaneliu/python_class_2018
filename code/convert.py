"""useful conversion functions"""


def c2f(c):
    """Celsius To Fahrenheit"""
    return c * 9. / 5. + 32.


def f2c(f):
    """Fahrenheit To Celsius"""
    return (f - 32.) * 5. / 9.


def km2mi(k):
    """kilometers To miles"""
    return k / 1.6


def mi2km(mi):
    """miles To kilometers"""
    return mi * 1.6

def kg2lb(kg):
    """kilograms to pounds"""
    return kg * 2.2

def lb2kg(lb):
    """pounds to kilograms"""
    return lb / 2.2

def _helper(x):
    """example of a 'private' function that should not
       be used outside of this module"""
    print(x)
    print("not for outside use")


# self test code that is run only if this module is run
# as a standalone program but not if the module is imported

if __name__ == "__main__":
    print("100 C is", c2f(100), "F")
    print("-40 F is", f2c(-40), "C")
    print("1.6 kilometers is", km2mi(1.6), "miles")
    print("1 miles is", mi2km(1), "kilometers")
    print("1 kilogram is", kg2lb(1), "pounds")
    print("2.2 pounds is", lb2kg(2.2), "kilograms")
