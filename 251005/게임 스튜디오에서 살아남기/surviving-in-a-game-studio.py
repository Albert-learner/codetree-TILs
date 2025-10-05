n = int(input())

# Please write your code here.
MOD = 10 ** 9 + 7
dp = [[[0] * 3 for _ in range(3)] for _ in range(n + 1)]
dp[0][0][0] = 1

for i in range(n):
    for t in range(3):
        for b in range(3):
            cur = dp[i][t][b]
            if not cur:
                continue

            dp[i + 1][t][0] = (dp[i + 1][t][0] + cur) % MOD

            if b + 1 < 3:
                dp[i + 1][t][b + 1] = (dp[i + 1][t][b + 1] + cur) % MOD

            if t + 1 < 3:
                dp[i + 1][t + 1][0] = (dp[i + 1][t + 1][0] + cur) % MOD

ans = 0
for t in range(3):
    for b in range(3):
        ans = (ans + dp[n][t][b]) % MOD

print(ans)