s = input()
t = input()

# Please write your code here.
n, m = len(s), len(t)

dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    si = s[i - 1]
    for j in range(1, m + 1):
        if si == t[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

lcs_len = dp[n][m]
scs_len = n + m - lcs_len
print(scs_len)