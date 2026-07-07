n, k = map(int, input().split())
cost = [int(input()) for _ in range(n)]
board = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
INF = 10 ** 18
size = 1 << n

dp = [INF] * size
dp[0] = 0

for mask in range(size):
    if dp[mask] == INF:
        continue

    for nxt in range(n):
        if mask & (1 << nxt):
            continue

        add_cost = cost[nxt]

        for cur in range(n):
            if mask & (1 << cur):
                add_cost = min(add_cost, board[cur][nxt])

        new_mask = mask | (1 << nxt)
        dp[new_mask] = min(dp[new_mask], dp[mask] + add_cost)

answer = INF
for mask in range(size):
    if mask.bit_count() >= k:
        answer = min(answer, dp[mask])

print(answer)