N, M = map(int, input().split())

def GCD(n, m):
    if n < m:
        n, m = m, n

    while m > 0:
        n, m = m, n % m

    return n

gcd = GCD(N, M)

print(N * M // gcd)