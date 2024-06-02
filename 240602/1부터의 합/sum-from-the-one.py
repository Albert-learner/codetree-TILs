N = int(input())

total, last = 0, 0
for i in range(1, 101):
    total += i

    if total >= N:
        last = i
        break

print(last)