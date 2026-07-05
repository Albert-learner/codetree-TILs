n = int(input())

# Please write your code here.
MOD = 10007

if n % 2 == 1:
    print(0)
else:
    dp = [0] * (n + 1)

    dp[0], dp[2] = 1, 3

    for i in range(4, n + 1, 2):
        dp[i] = (4 * dp[i - 2] - dp[i - 4]) % MOD

    print(dp[n])