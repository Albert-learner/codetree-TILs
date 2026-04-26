n, m = map(int, input().split())

horizontal = [list(map(int, input().split())) for _ in range(n)]
vertical = [list(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
parent = list(range(n * m))
rank = [0] * (n * m)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return False

    if rank[fa] < rank[fb]:
        fa, fb = fb, fa

    parent[fb] = fa
    if rank[fa] == rank[fb]:
        rank[fa] += 1

    return True

def node_id(r, c):
    return r * m + c

edges = []
for r in range(n):
    for c in range(m - 1):
        a = node_id(r, c)
        b = node_id(r, c + 1)
        w = horizontal[r][c]
        edges.append((w, a, b))

for r in range(n - 1):
    for c in range(m):
        a = node_id(r, c)
        b = node_id(r + 1, c)
        w = vertical[r][c]
        edges.append((w, a, b))

edges.sort()

answer = 0
used = 0
for w, a, b in edges:
    if union(a, b):
        answer += w
        used += 1

        if used == n * m - 1:
            break

print(answer)