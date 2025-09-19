n = int(input())

# Please write your code here.
dp = [0] * (n + 1)
dp[0] = 1
if n >= 1:
    dp[1] = 1

for i in range(2, n + 1):
    total = 0
    for left in range(i):
        right = i - 1 - left
        total += dp[left] * dp[right]
    dp[i] = total

print(dp[n])