n = int(input())
profit = list(map(int, input().split()))

# Please write your code here.
dp = [0] * (n + 1)

for length in range(1, n + 1):
    best = 0
    for cut in range(1, length + 1):
        best = max(best, profit[cut - 1] + dp[length - cut])
    dp[length] = best

print(dp[n])