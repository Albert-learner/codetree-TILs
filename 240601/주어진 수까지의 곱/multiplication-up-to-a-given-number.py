a, b = map(int, input().split())

prod = 1
for n in range(a, b + 1):
    prod *= n

print(prod)