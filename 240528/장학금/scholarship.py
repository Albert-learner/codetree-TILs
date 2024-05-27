mid, last = map(int, input().split())

if mid >= 90:
    if 95 <= last <= 100:
        print(100000)
    elif 90 <= last < 95:
        print(50000)
    else:
        print(0)
else:
    print(0)