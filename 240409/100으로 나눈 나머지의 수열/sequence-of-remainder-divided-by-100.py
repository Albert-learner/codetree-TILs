N = int(input())

def recur_seq(n):
    if n == 1:
        return 2
    elif n == 2:
        return 4

    return recur_seq(n - 2) * recur_seq(n - 1) % 100

print(recur_seq(N))