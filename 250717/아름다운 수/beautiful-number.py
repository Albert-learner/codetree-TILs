N = int(input())

def choose(count, n):
    if count >= n:
        return 1 if count == n else 0

    total = 0
    for i in range(1, 5):
        total += choose(count + i, n)

    return total

result = choose(0, N)
print(result)