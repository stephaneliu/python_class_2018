def add(x, y):
    return (x + y)

def subtract(x, y):
   return x - y

def devide(x, y):
    return x / y

def multiply(x, y):
    return x * y

operation_lookup = { '+':add, '-':subtract, '/':devide, '*':multiply }

def calculate(equation):
    x, operation, y = equation.split()
    return operation_lookup[operation](float(x), float(y))

print(calculate("1 + 2"))
print(calculate("1 - 2"))
print(calculate("1 / 2"))
print(calculate("1 * 2"))
