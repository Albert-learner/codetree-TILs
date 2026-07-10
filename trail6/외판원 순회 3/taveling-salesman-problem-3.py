n, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = 10 ** 18

dp = [[INF] * n for _ in range(1 << n)]
dp[1][0] = 0

for mask in range(1 << n):
    if mask.bit_count() > k + 1:
        continue

    for cur in range(n):
        if dp[mask][cur] == INF:
            continue

        if (mask >> cur) & 1 == 0:
            continue

        if mask.bit_count() == k + 1:
            continue

        for nxt in range(1, n):
            if (mask >> nxt) & 1:
                continue

            if A[cur][nxt] == 0:
                continue

            next_mask = mask | (1 << nxt)
            dp[next_mask][nxt] = min(
                dp[next_mask][nxt],
                dp[mask][cur] + A[cur][nxt]
            )

answer = INF
for mask in range(1 << n):
    if mask.bit_count() != k + 1:
        continue

    for last in range(1, n):
        if dp[mask][last] == INF:
            continue

        if A[last][0] == 0:
            continue

        answer = min(answer, dp[mask][last] + A[last][0])

print(answer)