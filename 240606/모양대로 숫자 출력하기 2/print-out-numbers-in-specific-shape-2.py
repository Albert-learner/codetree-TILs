N = int(input())

cnts = 2
for i in range(N):
    for j in range(N):
        print(cnts, end = ' ')
        cnts += 2
        if cnts > 8:
            cnts = 2
    print()