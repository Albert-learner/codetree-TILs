N = int(input())

for i in range(N):
    if i == 0:
        for _ in range(N):
            print('*', end = ' ')
    else:
        for j in range(N):
            if j % 2 == 1 and j >= i:
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
    print()