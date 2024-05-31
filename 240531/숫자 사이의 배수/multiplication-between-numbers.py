a, b = map(int, input().split())

totals = sum([n for n in range(a, b + 1) if n % 5 == 0 or n % 7 == 0])
avgs = round(totals / len([n for n in range(a, b + 1) if n % 5 == 0 or n % 7 == 0]), 1)

print(totals, avgs)