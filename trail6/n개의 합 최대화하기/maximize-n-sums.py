n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = float("-inf")

dp = [INF] * (1 << n)
dp[0] = 0

for i in range(n):
    next_dp = [INF] * (1 << n)
    
    for mask in range(1 << n):
        if dp[mask] == INF:
            continue

        if bin(mask).count("1") != i:
            continue

        for j in range(n):
            if (mask >> j) & 1:
                continue

            next_mask = mask | (1 << j)
            val = dp[mask] + grid[i][j]
            if val > next_dp[next_mask]:
                next_dp[next_mask] = val

    dp = next_dp

print(dp[(1 << n) - 1])