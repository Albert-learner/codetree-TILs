N = int(input())

prod, last = 1, 0
for n in range(1, 11):
    prod *= n
    if prod >= N:
        last = n
        break

print(last)