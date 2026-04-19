n, m = map(int, input().split())
a, b = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
from_v, to_v, satisfaction = zip(*edges)

# Please write your code here.
parent = list(range(n + 1))
rank = [0] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(x, y):
    rx = find(x)
    ry = find(y)
    if rx == ry:
        return
    
    if rank[rx] < rank[ry]:
        parent[rx] = ry
    elif rank[rx] > rank[ry]:
        parent[ry] = rx
    else:
        parent[ry] = rx
        rank[rx] += 1

edges.sort(key=lambda x: -x[2])

for u, v, s in edges:
    union(u, v)
    if find(a) == find(b):
        print(s)
        break