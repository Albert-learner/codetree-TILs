n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
NEG_INF = -10 ** 15
dp = [NEG_INF] * (n + 1)
dp[1] = 0

for i in range(1, n + 1):
    if dp[i] == NEG_INF:
        continue

    max_jump = arr[i - 1]
    for j in range(1, max_jump + 1):
        ni = i + j
        if ni <= n:
            dp[ni] = max(dp[ni], dp[i] + 1)

print(max(dp[1:]))