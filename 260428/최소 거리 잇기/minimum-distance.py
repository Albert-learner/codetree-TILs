n, m = map(int, input().split())

x = []
y = []
for _ in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)

edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import math

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

for a, b in edges:
    union(a, b)

all_edges = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        dx = x[i - 1] - x[j - 1]
        dy = y[i - 1] - y[j - 1]
        dist = math.sqrt(dx ** 2 + dy ** 2)
        all_edges.append((dist, i, j))

all_edges.sort()

answer = 0.0
for dist, a, b in all_edges:
    if union(a, b):
        answer += dist

print(f"{answer:.2f}")