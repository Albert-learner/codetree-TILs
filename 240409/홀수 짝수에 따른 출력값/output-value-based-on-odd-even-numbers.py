N = int(input())

def print_sum(n):
    if n == 0 or n == 1:
        return n

    if n % 2 == 0:
        return n + print_sum(n - 2)
    else:
        return n + print_sum(n - 2)

print(print_sum(N))