n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

parents = [0] * (n + 1)
visited = [False] * (n + 1)

queue = deque([1])
visited[1] = True

while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if not visited[nxt]:
            visited[nxt] = True
            parents[nxt] = cur
            queue.append(nxt)

for i in range(2, n + 1):
    print(parents[i])