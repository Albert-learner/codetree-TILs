n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

# Please write your code here.
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    root = x
    while parent[root] != root:
        root = parent[root]

    while parent[x] != x:
        nxt = parent[x]
        parent[x] = root
        x = nxt

    return root

def union(a, b):
    fa = find(a)
    fb = find(b)

    if fa == fb:
        return

    if size[fa] < size[fb]:
        fa, fb = fb, fa

    parent[fb] = fa
    size[fa] += size[fb]

for a, b in edges:
    union(a, b)

root = find(path[0])
for node in path[1:]:
    if find(node) != root:
        print(0)
        break
    else:
        print(1)

    