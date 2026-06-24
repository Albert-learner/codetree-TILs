n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x = [p[0] for p in points]
y = [p[1] for p in points]

# Please write your code here.
points.sort()

def dist(i, j):
    x1, y1 = points[i]
    x2, y2 = points[j]
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

INF = 10 ** 30

dp = {(0, 0): [0, INF]}

for nxt in range(1, n):
    new_dp = {}

    for (a, b), (cost0, cost1) in dp.items():
        d1 = dist(a, nxt)
        d2 = dist(b, nxt)

        state = (nxt, b)
        if state not in new_dp:
            new_dp[state] = [INF, INF]

        if cost0 != INF:
            new_dp[state][0] = min(new_dp[state][0], cost0 + d1)
            new_dp[state][1] = min(new_dp[state][1], cost0) 

        if cost1 != INF:
            new_dp[state][1] = min(new_dp[state][1], cost1 + d1)

        state = (a, nxt)
        if state not in new_dp:
            new_dp[state] = [INF, INF]

        if cost0 != INF:
            new_dp[state][0] = min(new_dp[state][0], cost0 + d2)
            new_dp[state][1] = min(new_dp[state][1], cost0)

        if cost1 != INF:
            new_dp[state][1] = min(new_dp[state][1], cost1 + d2)

    dp = new_dp

answer = INF

for (a, b), (cost0, cost1) in dp.items():
    d = dist(a, b)

    answer = min(answer, cost1 + d)
    answer = min(answer, cost0)

print(answer)