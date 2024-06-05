N = int(input())

for i in range(N):
    if i == 0 or i == N - 1:
        print("* " * N)
    else:
        for j in range(N):
            if i > j or j == N - 1:
                print('*', end = ' ')
            elif i <= j:
                print(' ', end = ' ')