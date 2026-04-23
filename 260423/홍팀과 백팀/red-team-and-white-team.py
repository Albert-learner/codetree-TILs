n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import sys
from collections import deque

adj = [[] for _ in range(n + 1)]
for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

color = [0] * (n + 1)

for start in range(1, n + 1):
    if color[start] != 0:
        continue

    queue = deque([start])
    color[start] = 1

    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if color[v] == 0:
                color[v] = -color[u]
                queue.append(v)
            elif color[v] == color[u]:
                print(0)
                sys.exit()

print(1)