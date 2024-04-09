A, B = map(int, input().split())

def operate(a, b):
    if a < b:
        a += 10
        b *= 2
    else:
        b += 10
        a *= 2

    return a, b

print(*operate(A, B))