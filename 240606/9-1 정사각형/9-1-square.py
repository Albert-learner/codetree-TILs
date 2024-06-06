N = int(input())

cnts = 9
for i in range(N):
    for j in range(N):
        print(cnts, end = '')
        cnts -= 1
        if cnts < 1:
            cnts = 9
    print()