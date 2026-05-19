n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
import heapq

reverse_graph = [[] for _ in range(n + 1)]
outdegree = [0] * (n + 1)

for x, y in edges:
    reverse_graph[y].append(x)
    outdegree[x] += 1

pq = []
for i in range(1, n + 1):
    if outdegree[i] == 0:
        heapq.heappush(pq, -i)

answer = [0] * (n + 1)
num = n
visited_count = 0

while pq:
    cur = -heapq.heappop(pq)

    answer[cur] = num
    num -= 1
    visited_count += 1

    for prev in reverse_graph[cur]:
        outdegree[prev] -= 1

        if outdegree[prev] == 0:
            heapq.heappush(pq, -prev)

if visited_count != n:
    print(-1)
else:
    print(*answer[1:])