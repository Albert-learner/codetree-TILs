str = input()

# Please write your code here.
n = len(str)

dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for length in range(2, n + 1):
    for i in range(n - length + 1):
        j = i + length - 1

        if str[i] == str[j]:
            if length == 2:
                dp[i][j] =2
            else:
                dp[i][j] = dp[i + 1][j - 1] + 2
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

print(n - dp[0][n - 1])