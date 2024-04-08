N, M = map(int, input().split())

def GCD(n, m):
    if n < m:
        n, m = m, n

    while m > 0:
        n, m = m, n % m

    print(n)

GCD(N, M)