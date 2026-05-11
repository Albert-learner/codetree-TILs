n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for a, b in edges:
    graph[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

answer = []

while q:
    cur = q.popleft()
    answer.append(cur)

    for nxt in graph[cur]:
        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

print(*answer)