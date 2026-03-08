n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
INF = 10 ** 15

dist = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for a, b, c in edges:
    if c < dist[a][b]:
        dist[a][b] = c

for k in range(1, n + 1):
    dk = dist[k]
    for i in range(1, n + 1):
        if dist[i][k] == INF:
            continue
        di = dist[i]
        ik = di[k]
        for j in range(1, n + 1):
            nd = ik + dk[j]
            if nd < di[j]:
                di[j] = nd

answer = INF
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i != j and dist[i][j] != INF and dist[j][i] != INF:
            answer = min(answer, dist[i][j] + dist[j][i])

print(answer)