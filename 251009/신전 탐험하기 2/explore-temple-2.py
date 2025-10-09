n = int(input())
l, m, r = [], [], []

for _ in range(n):
    left, mid, right = map(int, input().split())
    l.append(left)
    m.append(mid)
    r.append(right)

# Please write your code here.
vals = list(zip(l, m, r))
NEG = -10 ** 18
ans = 0

for s in range(3):
    dp = [[NEG] * 3 for _ in range(n)]
    dp[0][s] = vals[0][s]
    for i in range(1, n):
        for d in range(3):
            dp[i][d] = vals[i][d] + max(dp[i - 1][(d + 1) % 3],
                                        dp[i - 1][(d + 2) % 3])

    best_last = max(dp[n - 1][(s + 1) % 3],
                    dp[n - 1][(s + 2) % 3])
    ans = max(ans, best_last)

print(ans)