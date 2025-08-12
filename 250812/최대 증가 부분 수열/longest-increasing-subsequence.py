n = int(input())
m = list(map(int, input().split()))

# Please write your code here.
nums = [0] + m
dp = [0] * (n + 1)

for i in range(1, n + 1):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))