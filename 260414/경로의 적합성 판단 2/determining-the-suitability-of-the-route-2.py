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
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]

for a, b in edges:
    union(a, b)

root = find(path[0])
for node in path[1:]:
    if find(node) != root:
        print(0)
        break
else:
    print(1)