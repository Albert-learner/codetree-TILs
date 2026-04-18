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

    if fa != fb:
        parent[fb] = fa

for u, v in edges:
    union(u, v)

components = set()
for i in range(1, n + 1):
    components.add(find(i))

c = len(components)
answer = (m - (n - c)) + (c - 1)
print(answer)