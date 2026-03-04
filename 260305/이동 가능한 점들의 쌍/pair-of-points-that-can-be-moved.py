N, M, P, Q = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(M)]
queries = [tuple(map(int, input().split())) for _ in range(Q)]

# Please write your code here.
INF = 10 ** 18

dist0 = [[INF] * (N + 1) for _ in range(N + 1)]
dist1 = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    if i <= P:
        dist1[i][i] = 0
    else:
        dist0[i][i] = 0

for u, v, w in edges:
    if v <= P:
        dist1[u][v] = min(dist1[u][v], w)
    else:
        dist0[u][v] = min(dist0[u][v], w)

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if dist0[i][k] + dist0[k][j] < dist0[i][j]:
                dist0[i][j] = dist0[i][k] + dist0[k][j]

            dist1[i][j] = min(
                dist1[i][j],
                dist1[i][k] + dist0[k][j],
                dist0[i][k] + dist1[k][j],
                dist1[i][k] + dist1[k][j]
            )

cnts, total_csts = 0, 0

for a, b in queries:
    if dist1[a][b] < INF:
        cnts += 1
        total_csts += dist1[a][b]

print(cnts)
print(total_csts)
