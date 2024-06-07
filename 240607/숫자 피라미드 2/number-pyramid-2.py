N = int(input())

cnts = 1
for i in range(1, N + 1):
    for j in range(i):
        print(cnts, end = ' ')
        cnts += 1
    print()