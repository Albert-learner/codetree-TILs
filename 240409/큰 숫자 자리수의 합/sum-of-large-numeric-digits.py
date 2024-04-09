A, B, C = map(int, input().split())

mul_three = A * B * C

def add_all(total):
    if total < 10:
        return total

    return add_all(total // 10) + total % 10

print(add_all(mul_three))