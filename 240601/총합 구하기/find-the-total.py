a, b = map(int, input().split())

print(sum([n for n in range(a, b + 1) if n % 6 == 0 and n % 8 != 0]))