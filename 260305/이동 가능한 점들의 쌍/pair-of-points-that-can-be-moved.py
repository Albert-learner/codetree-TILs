N, M, P, Q = map(int, input().split())

# Please write your code here.
INF = 10 ** 18

dist = [[INF] * (N + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    dist[i][i] = 0

for _ in range(M):
    u, v, w = map(int, input().split())
    if w < dist[u][v]:
        dist[u][v] = w

queries = [tuple(map(int, input().split())) for _ in range(Q)]

for k in range(1, N + 1):
    dk = dist[k]
    for i in range(1, N + 1):
        dik = dist[i][k]
        if dik == INF:
            continue
        di = dist[i]
        base = dik
        # j 루프
        for j in range(1, N + 1):
            nd = base + dk[j]
            if nd < di[j]:
                di[j] = nd

count = 0
total_cost = 0

for a, b in queries:
    best = INF
    da = dist[a]
    for r in range(1, P + 1):
        if da[r] == INF or dist[r][b] == INF:
            continue
        cand = da[r] + dist[r][b]
        if cand < best:
            best = cand

    if best != INF:
        count += 1
        total_cost += best

print(count)
print(total_cost)