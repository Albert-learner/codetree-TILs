N = int(input())

def recur_seq(n):
    if n == 1:
        return 0

    if n % 2 == 0:
        return recur_seq(n // 2) + 1
    else:
        return recur_seq(n * 3 + 1) + 1

print(recur_seq(N))