n, m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
items = list(map(int, input().split()))

# Please write your code here.
import sys
sys.setrecursionlimit(200000)

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

has_item = [False] * (n + 1)
for x in items:
    has_item[x] = True

parent = [0] * (n + 1)
order = []
stack = [1]
parent[1] = -1

while stack:
    u = stack.pop()
    order.append(u)
    for v in graph[u]:
        if v == parent[u]:
            continue

        parent[v] = u
        stack.append(v)

INF = 10 ** 18
dp0 = [0] * (n + 1)
dp1 = [0] * (n + 1)

for u in reversed(order):
    if has_item[u]:
        dp0[u] = INF
        dp1[u] = 0
    else:
        dp0[u] = 0
        dp1[u] = 1

    for v in graph[u]:
        if v == parent[u]:
            continue

        dp0[u] += dp1[v]

        dp1[u] += min(dp0[v], dp1[v])

print(min(dp0[1], dp1[1]))