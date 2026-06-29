n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
INF = -10 ** 18
MAXV = 10

dp = [[[INF] * (MAXV + 1) for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i][arr[i]] = 0

for length in range(2, n + 1):
    for l in range(n - length + 1):
        r = l + length - 1

        for mid in range(l, r):
            left = dp[l][mid]
            right = dp[mid + 1][r]

            for a in range(MAXV + 1):
                if left[a] == INF:
                    continue

                for b in range(MAXV + 1):
                    if right[b] == INF:
                        continue

                    v = abs(a - b)
                    score = left[a] + right[b] + a + b

                    if score > dp[l][r][v]:
                        dp[l][r][v] = score

print(max(dp[0][n - 1]))