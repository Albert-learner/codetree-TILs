n, m = map(int, input().split())

edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]

for a, b, d in edges:
    graph[a].append((b, d))
    graph[b].append((a, d))

def get_distance(start, end):
    if start == end:
        return 0

    visited = [False] * (n + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        cur, dist = queue.popleft()
        if cur == end:
            return dist

        for nxt, d in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, dist + d))

for a, b in queries:
    print(get_distance(a, b))
