N = int(input())
n_lst = list(map(int, input().split()))

def GCD(a, b):
    if a % b == 0:
        return b

    return GCD(b, a % b)

def LCM(n):
    if n == 0:
        return n_lst[0]
    elif n == 1:
        return (n_lst[0] * n_lst[1]) // (GCD(n_lst[0], n_lst[1]))

    minus = LCM(n - 1)
    return minus * n_lst[n] // GCD(minus, n_lst[n])

print(LCM(N - 1))