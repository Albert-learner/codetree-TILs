expression = input()

# Please write your code here.
from itertools import product

tokens = [ch for ch in expression]

vars_used = sorted({t for t in tokens if t.isalpha()})

def apply_op(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y

    return x * y

def eval_with(assign):
    val = assign[tokens[0]]

    i = 1
    while i < len(tokens):
        op = tokens[i]
        y = assign[tokens[i + 1]]
        val = apply_op(val, op, y)
        i += 2

    return val

max_result = -(1 << 60)
for values in product(range(1, 5), repeat = len(vars_used)):
    assign = {var:v for var, v in zip(vars_used, values)}
    max_result = max(max_result, eval_with(assign))

print(max_result)