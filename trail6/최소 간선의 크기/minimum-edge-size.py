n, m = map(int, input().split())
a, b = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
from_v, to_v, satisfaction = zip(*edges)

# Please write your code here.
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return

    if size[fa] < size[fb]:
        fa, fb = fb, fa

    parent[fb] = fa
    size[fa] += size[fb]

edges.sort(key = lambda x: x[2], reverse = True)

for x, y, s in edges:
    union(x, y)

    if find(a) == find(b):
        print(s)
        break