n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from collections import deque

def has_cycle(limit):
    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for i in range(limit):
        a, b = edges[i]
        graph[a].append(b)
        indegree[b] += 1

    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    cnt = 0
    while q:
        cur = q.popleft()
        cnt += 1

        for nxt in graph[cur]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)

    return cnt != n

if not has_cycle(m):
    print("Consistent")
else:
    left, right = 1, m
    answer = m

    while left <= right:
        mid = (left + right) // 2

        if has_cycle(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)