n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
points.sort()

def dist(i, j):
    x1, y1 = points[i]
    x2, y2 = points[j]

    return (x1 - x2) ** 2 + (y1 - y2) ** 2

INF = 10 ** 18

dp = [[INF] * n for _ in range(n)]

dp[0][1] = dist(0, 1)

for j in range(2, n):
    for i in range(0, j - 1):
        dp[i][j] = dp[i][j - 1] + dist(j - 1, j)

    for i in range(0, j - 1):
        dp[j - 1][j] = min(
            dp[j - 1][j],
            dp[i][j - 1] + dist(i, j)
        )
        

answer = dp[n - 2][n - 1] + dist(n - 2, n - 1)

print(answer)