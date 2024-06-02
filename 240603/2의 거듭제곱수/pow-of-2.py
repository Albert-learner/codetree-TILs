N = int(input())

cnts = 0
while N >= 2:
    N //= 2
    cnts += 1

print(cnts)