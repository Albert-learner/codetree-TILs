N = int(input())

cnts = 1
for i in range(N, 0, -1):
    for j in range(N, 0, -1):
        if j > i:
            print('  ', end = '')
        else:
            print(cnts, end = ' ')
            cnts += 1

            if cnts == 10:
                cnts = 1
    print()