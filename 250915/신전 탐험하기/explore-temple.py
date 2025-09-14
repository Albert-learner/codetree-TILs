n = int(input())
l, m, r = [], [], []
for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.
vals = list(zip(l, m, r))
dp = [[0] * 3 for _ in range(n)]
dp[0][0], dp[0][1], dp[0][2] = vals[0]

for i in range(1, n):
    for d in range(3):
        dp[i][d] = vals[i][d] + max(dp[i - 1][(d + 1) % 3], dp[i - 1][(d + 2) % 3])

print(max(dp[n - 1]))