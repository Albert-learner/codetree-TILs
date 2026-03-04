n, m = map(int, input().split())

# Create 2D list with 1-based indexing
dist = [[0] * (n + 1) for _ in range(n + 1)]

# Read distance matrix
for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(n):
        dist[i][j + 1] = row[j]

# Read queries
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
for k in range(1, n + 1):
    dk = dist[k]
    for i in range(1, n + 1):
        dik = dist[i][k]
        di = dist[i]
        for j in range(1, n + 1):
            nd = dik + dk[j]
            if nd < di[j]:
                di[j] = nd

out = []
for a, b in queries:
    out.append(str(dist[a][b]))
print("\n".join(out))