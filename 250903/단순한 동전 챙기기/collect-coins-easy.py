n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
S = E = None
coins = []
for i in range(n):
    for j in range(n):
        ch = grid[i][j]
        if ch == 'S':
            S = (i, j)
        elif ch == 'E':
            E = (i, j)
        elif ch.isdigit():
            coins.append((int(ch), i, j))

if len(coins) < 3:
    print(-1)
    raise SystemExit

coins.sort(key=lambda x: x[0])

def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

C = len(coins)
INF = 10 ** 9

dp = [[INF] * (C + 1) for _ in range(C)]

for i in range(C):
    dp[i][1] = dist(S, (coins[i][1], coins[i][2]))

for i in range(C):
    xi = (coins[i][1], coins[i][2])
    for k in range(2, C + 1):
        best = INF
        for j in range(i):
            if dp[j][k - 1] == INF:
                continue

            xj = (coins[j][1], coins[j][2])
            best = min(best, dp[j][k - 1] + dist(xj, xi))
        dp[i][k] = best

ans = INF
for i in range(C):
    xi = (coins[i][1], coins[i][2])
    to_E = dist(xi, E)
    for k in range(3, C + 1):
        if dp[i][k] != INF:
            ans = min(ans, dp[i][k] + to_E)

print(ans if ans != INF else -1)