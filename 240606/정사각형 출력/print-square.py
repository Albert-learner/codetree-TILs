N = int(input())

for i in range(1, N ** 2 + 1):
    if i % N == 0:
        print(i)
    else:
        print(i, end = ' ')