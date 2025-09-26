n = int(input())
jobs = [tuple(map(int, input().split())) for _ in range(n)]
jobs.sort(key = lambda x: x[1])

s = [job[0] for job in jobs]
e = [job[1] for job in jobs]
p = [job[2] for job in jobs]

# Please write your code here.
from bisect import bisect_left

dp = [0] * (n + 1)
ends = e[:]

for i in range(1, n + 1):
    si, pi = s[i - 1], p[i - 1]
    j = bisect_left(ends, si) - 1
    take = pi + (dp[j + 1] if j >= 0 else 0)
    skip = dp[i - 1]
    dp[i] = max(take, skip)

print(dp[n])