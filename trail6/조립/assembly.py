import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
x, y, z = [], [], []

for _ in range(m):
    a, b, c = map(int, input().split())
    x.append(a)
    y.append(b)
    z.append(c)

# Please write your code here.

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for i in range(m):
    graph[y[i]].append((x[i], z[i]))
    indegree[x[i]] += 1

need = [[0] * (n + 1) for _ in range(n + 1)]

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        need[i][i] = 1
        q.append(i)

while q:
    cur = q.popleft()

    for nxt, cnt in graph[cur]:
        for base in range(1, n + 1):
            need[nxt][base] += need[cur][base] * cnt

        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

answer = []

for i in range(1, n + 1):
    if need[n][i] > 0:
        answer.append(f"{i} {need[n][i]}")

print("\n".join(answer))