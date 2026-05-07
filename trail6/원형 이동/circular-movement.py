n, m, k = map(int, input().split())
cost = [0] + list(map(int, input().split()))
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return

    if size[ra] < size[rb]:
        ra, rb = rb, ra

    parent[rb] = ra
    size[ra] += size[rb]

blocked = set()

for a, b in edges:
    if a > b:
        a, b = b, a
    blocked.add((a, b))

for i in range(1, n + 1):
    nxt = i + 1
    if nxt == n + 1:
        nxt = 1

    a, b = i, nxt
    if a > b:
        a, b = b, a

    if (a, b) not in blocked:
        union(i, nxt)

components = {}

for i in range(1, n + 1):
    r = find(i)

    if r not in components:
        components[r] = []

    components[r].append(i)

if len(components) == 1:
    print(1)
else:
    total = 0

    for nodes in components.values():
        mn = min(cost[x] for x in nodes)
        total += mn

    if total <= k:
        print(1)
    else:
        print(0)