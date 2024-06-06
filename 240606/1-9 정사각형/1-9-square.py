N = int(input())

for i in range(1, N ** 2 + 1):
    if i % N == 0:
        if i >= 10:
            print(i % 10 + 1)
        else:
            print(i % 10)
    else:
        if i >= 10:
            print(i % 10 + 1, end = '')
        else:
            print(i % 10, end = '')