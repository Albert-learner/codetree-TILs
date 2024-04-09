N = int(input())

def recur_sum(n):
    if n == 1:
        return 1

    return recur_sum(n - 1) + n

print(recur_sum(N))