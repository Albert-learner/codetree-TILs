n = int(input())
direct = [int(input()) for _ in range(n)]
cost = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [False] * n

min_cost = direct[:]

answer = 0

for _ in range(n):
    u = -1
    best = 10 ** 18

    for i in range(n):
        if not visited[i] and min_cost[i] < best:
            best = min_cost[i]
            u = i

    visited[u] = True
    answer += best

    for v in range(n):
        if not visited[v] and cost[u][v] < min_cost[v]:
            min_cost[v] = cost[u][v]

print(answer)
