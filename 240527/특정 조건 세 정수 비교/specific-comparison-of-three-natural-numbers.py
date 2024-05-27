a, b, c = map(int, input().split())

if a == min([a, b, c]):
    print(1, end = ' ')
else:
    print(0, end = ' ')

if a == b and b == c and c == a:
    print(1, end = ' ')
else:
    print(0, end = ' ')