n, m1, m2 = map(int, input().split())

directed_edges = [tuple(map(int, input().split())) for _ in range(m1)]
undirected_edges = [tuple(map(int, input().split())) for _ in range(m2)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for a, b in directed_edges:
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

visited_cnt = 0
while q:
    cur = q.popleft()
    visited_cnt += 1

    for nxt in graph[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            q.append(nxt)

if visited_cnt == n:
    print("Yes")
else:
    print("No")