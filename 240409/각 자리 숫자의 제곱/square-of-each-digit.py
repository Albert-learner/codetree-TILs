N = int(input())

def power_sum(n):
    if n < 10:
        return n ** 2

    return power_sum(n // 10) + (n % 10) ** 2

print(power_sum(N))