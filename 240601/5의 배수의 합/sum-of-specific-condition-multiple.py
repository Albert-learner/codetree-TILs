a, b = map(int, input().split())

print(sum([n if n % 5 == 0 else 0 for n in range(a, b + 1) ]))