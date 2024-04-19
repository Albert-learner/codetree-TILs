N = int(input())
a, b, c = map(int, input().split())

min_comb = min([a, b, c])
answer = N ** 3
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if i - a >= 3 and j - b >= 3 and k - c >= 3:
                answer -= 1

print(answer)