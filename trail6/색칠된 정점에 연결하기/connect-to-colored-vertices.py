n, m, k = map(int, input().split())
colored = list(map(int, input().split()))
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

for node in colored:
    union(0, node)

edges.sort(key = lambda x: x[2])

answer = 0
for u, v, w in edges:
    if union(u, v):
        answer += w

print(answer)