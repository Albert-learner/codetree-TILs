n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
dp = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(n - 1, -1, -1):
    ai = a[i]
    for j in range(m - 1, -1, -1):
        if ai == b[j]:
            dp[i][j] = dp[i + 1][j + 1] + 1
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

L = dp[0][0]
if L == 0:
    print()
    exit()

posB = {b[j]: j for j in range(m)}

i = j = 0
ans = []
while len(ans) < L:
    best_val = None
    best_i = best_j = -1
    for ii in range(i, n):
        v = a[ii]
        jj = posB.get(v, -1)
        if jj != -1 and jj >= j:
            if 1 + dp[ii + 1][jj + 1] == dp[i][j]:
                if best_val is None or v < best_val:
                    best_val = v
                    best_i, best_j = ii, jj

    ans.append(best_val)
    i, j = best_i + 1, best_j + 1

print(*ans)