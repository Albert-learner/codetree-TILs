n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
parent = list(range(n + 1))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa, fb = find(a), find(b)

    if fa == fb:
        return False

    parent[fb] = fa
    return True

edges.sort(key = lambda x: x[2])

total = 0
max_edge = 0
used = 0

for a, b, w in edges:
    if union(a, b):
        total += w
        max_edge = max(max_edge, w)
        used += 1

        if used == n - 1:
            break

print(total - max_edge)
