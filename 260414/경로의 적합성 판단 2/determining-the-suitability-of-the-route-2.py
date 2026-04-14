n, m, k = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(m)]
path = list(map(int, input().split()))

# Please write your code here.
parent = list(range(n + 1))

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])

    return parent[x]

def union(a, b):
    fa = find(a)
    fb = find(b)

    if fa == fb:
        return

    if fa != fb:
        parent[fb] = fa

for a, b in edges:
    union(a, b)

root = find(path[0])
for node in path[1:]:
    if find(node) != root:
        print(0)
        break
    else:
        print(1)

    