def add(a, b):
    return a + b

def diff(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a // b

a, o, c = input().split()
a, c = int(a), int(c)
if o in ['+', '-', '/', '*']:
    if o == '+':
        print(a, o, c, "= {}".format(add(a, c)))
    elif o == '-':
        print(a, o, c, "= {}".format(diff(a, c)))
    elif o == '*':
        print(a, o, c, "= {}".format(multiply(a, c)))
    else:
        print(a, o, c, "= {}".format(divide(a, c)))
else:
    print(False)