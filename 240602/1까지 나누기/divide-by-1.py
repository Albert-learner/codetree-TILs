N = int(input())

idx, cnts = 1, 0
while N // idx > 1:
    N //= idx
    cnts += 1
    idx += 1

print(cnts + 1)