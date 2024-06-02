N = int(input())

idx, cnts = 1, 0
while N >= 1:
    N //= idx
    idx += 1
    cnts += 1

print(cnts)