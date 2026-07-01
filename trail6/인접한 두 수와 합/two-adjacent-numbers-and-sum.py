n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + arr[i]

def range_sum(l, r):
    return prefix[r + 1] - prefix[l]

dp = [[0] * n for _ in range(n)]

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1
        total = range_sum(l, r)
        best = 0

        for k in range(l, r):
            left_sum = range_sum(l, k)
            right_sum = total - left_sum

            score = dp[l][k] + dp[k + 1][r] + abs(left_sum - right_sum)
            if score > best:
                best = score

        dp[l][r] = best

print(dp[0][n - 1])