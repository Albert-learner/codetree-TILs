N = int(input())

for i in range(1, N ** 2 + 1):
    if i < 10:
        if i % N == 0:
            print(i)
        else:
            print(i, end = '')
    else:
        q, r = divmod(i, 10)
        if i % N == 0:
            print(q + r)
        else:
            print(q + r, end = '')