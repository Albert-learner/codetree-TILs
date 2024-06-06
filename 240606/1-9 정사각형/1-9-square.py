N = int(input())

cnts = 1
for i in range(N):
    for j in range(N):
        print(cnts, end = '')
        cnts += 1
        if cnts > 9:
            cnts = 1
    print()