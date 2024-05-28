a, b, c = map(int, input().split())

# lst = sorted([a, b, c])

# print(lst[1])

if b > c:
    if b > a and a > c:
        print(a)
else:
    if c > a and a > b:
        print(a)

if a > c:
    if a > b and b > c:
        print(b)
else:
    if b > a and c > b:
        print(b)

if a > b:
    if a > c and c > b:
        print(c)
else:
    if b > c and c > a:
        print(c)