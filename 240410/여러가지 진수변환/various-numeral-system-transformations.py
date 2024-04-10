N, bit = map(int, input().split())

digits = []
while True:
    if N < bit:
        digits.append(N)
        break

    digits.append(N % bit)
    N //= bit

print("".join(map(str, digits[::-1])))