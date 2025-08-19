n = int(input())

# Please write your code here.
dp = [0] * (n + 1)
dp[0] = 1
nums = [1, 2, 5]

for i in range(1, n + 1):
    for num in nums:
        if i - num >= 0:
            dp[i] += dp[i - num]

print(dp[n])