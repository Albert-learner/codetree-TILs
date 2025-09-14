n = int(input())

# Please write your code here.
MOD = 10 ** 9 + 7

dp = [1 if i != 0 else 0 for i in range(10)]

for _ in range(2, n + 1):
    ndp = [0] * 10
    ndp[0] = dp[1] % MOD
    ndp[9] = dp[8] % MOD
    for d in range(1, 9):
        ndp[d] = (dp[d - 1] + dp[d + 1]) % MOD
    dp = ndp

print(sum(dp) % MOD if n > 1 else 9)