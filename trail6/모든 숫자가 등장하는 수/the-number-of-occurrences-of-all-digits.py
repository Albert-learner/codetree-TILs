n = int(input())

# Please write your code here.
MOD = 10007
FULL = (1 << 10) - 1

dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(n + 1)]

for d in range(1, 10):
    dp[1][d][1 << d] = 1

for length in range(1, n):
    for last in range(10):
        for mask in range(1 << 10):
            val = dp[length][last][mask]
            if val == 0:
                continue

            for nxt in (last - 1, last + 1):
                if 0 <= nxt <= 9:
                    new_mask = mask | (1 << nxt)
                    dp[length + 1][nxt][new_mask] += val
                    dp[length + 1][nxt][new_mask] %= MOD

answer = 0

for last in range(10):
    answer = (answer + dp[n][last][FULL]) % MOD

print(answer)