n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for a, b in edges:
    graph[a].append(b)
    indegree[b] += 1

pressure = [1] * (n + 1)

max_pressure = [0] * (n + 1)
max_cnt = [0] * (n + 1)

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        p = pressure[cur]

        if p > max_pressure[nxt]:
            max_pressure[nxt] = p
            max_cnt[nxt] = 1
        elif p == max_pressure[nxt]:
            max_cnt[nxt] += 1

        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            if max_cnt[nxt] >= 2:
                pressure[nxt] = max_pressure[nxt] + 1
            else:
                pressure[nxt] = max_pressure[nxt]

            q.append(nxt)

print(max(pressure))