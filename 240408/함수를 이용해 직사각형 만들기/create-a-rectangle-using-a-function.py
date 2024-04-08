def print_mn_stars(m, n):
    for row in range(m):
        print('1' * n)

N, M = map(int, input().split())
print_mn_stars(N, M)