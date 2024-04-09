N = int(input())

def strange_seq(n):
    if n == 1 or n == 2:
        return n

    return strange_seq(int(n / 3)) + strange_seq(n - 1)

print(strange_seq(N))