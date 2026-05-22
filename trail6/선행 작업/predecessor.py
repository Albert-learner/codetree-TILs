n = int(input())
time = []
prereq_count = []
prereq = []

for _ in range(n):
    line = list(map(int, input().split()))
    time.append(line[0])
    prereq_count.append(line[1])
    prereq.append(line[2:])

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

for task in range(1, n + 1):
    for pre in prereq[task - 1]:
        graph[pre].append(task)
        indegree[task] += 1

finish_time = [0] * (n + 1)

q = deque()
for i in range(1, n + 1):
    if indegree[i] == 0:
        finish_time[i] = time[i - 1]
        q.append(i)

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        finish_time[nxt] = max(
            finish_time[nxt],
            finish_time[cur] + time[nxt - 1]
        )

        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

print(max(finish_time))