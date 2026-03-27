import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline

n, r, q = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
U = [int(input()) for _ in range(q)]

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

parent = [0] * (n + 1)
order = []

stack = [r]
parent[r] = -1

while stack:
    cur = stack.pop()
    order.append(cur)
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue
        parent[nxt] = cur
        stack.append(nxt)

subtree_size = [1] * (n + 1)

for cur in reversed(order):
    for nxt in graph[cur]:
        if nxt == parent[cur]:
            continue
        subtree_size[cur] += subtree_size[nxt]

for u in U:
    print(subtree_size[u])