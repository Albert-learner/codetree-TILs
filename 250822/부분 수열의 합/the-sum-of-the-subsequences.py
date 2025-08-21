n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
INT_MAX = 10 ** 18
dp = [INT_MAX] * (m + 1)
dp[0] = 0

for num in A:
    for j in range(m, num - 1, -1):
        if dp[j - num] != INT_MAX:
            dp[j] = min(dp[j], dp[j - num] + 1)

print("Yes" if INT_MAX not in dp else "No")