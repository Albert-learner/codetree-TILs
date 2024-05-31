a, b = map(int, input().split())

if a > b:
    a, b = b, a

print(sum([n  for n in range(a, b + 1) if n % 5 == 0]))