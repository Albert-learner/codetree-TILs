N, M = map(int, input().split())
a = [0] + list(map(int, input().split()))

# Please write your code here.
NEG = -10 ** 9
dp = [[[NEG] * (M + 1) for _ in range(5)] for _ in range(N + 1)]

for v in range(1, 5):
    dp[1][v][0] = 1 if v == a[1] else 0

for i in range(2, N + 1):
    for prev in range(1, 5):
        for t in range(M + 1):
            if dp[i - 1][prev][t] == NEG:
                continue

            for cur in range(1, 5):
                nt = t + (prev != cur)
                if nt > M:
                    continue

                gain = 1 if cur == a[i] else 0
                if dp[i][cur][nt] < dp[i - 1][prev][t] + gain:
                    dp[i][cur][nt] = dp[i - 1][prev][t] + gain

ans = max(dp[N][v][t] for v in range(1, 5) for t in range(M+1))
print(ans)