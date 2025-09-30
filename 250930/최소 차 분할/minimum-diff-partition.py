n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
total_sum = sum(arr)
max_sum = total_sum // 2

dp = [False] * (max_sum + 1)
dp[0] = True

for n in arr:
    for i in range(max_sum, n - 1, -1):
        dp[i] |= dp[i - n]

min_diff = max_sum
for i in range(max_sum, -1, -1):
    if dp[i]:
        min_diff = min(min_diff, total_sum - 2 * i)
        break

print(min_diff)