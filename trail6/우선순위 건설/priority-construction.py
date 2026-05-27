n = int(input())
t = []
prev_build = [[] for _ in range(500)]
prev_count = [0] * 500

for i in range(n):
    nums = list(map(int, input().split()))
    t.append(nums[0])
    prev_build[i] = [x - 1 for x in nums[1:-1]]
    prev_count[i] = len(prev_build[i])

# Please write your code here.
from collections import deque

graph = [[] for _ in range(n)]
indegree = [0] * n

for i in range(n):
    indegree[i] = prev_count[i]

    for prev in prev_build[i]:
        graph[prev].append(i)

finish_time = [0] * n

q = deque()

for i in range(n):
    if indegree[i] == 0:
        finish_time[i] = t[i]
        q.append(i)

while q:
    cur = q.popleft()

    for nxt in graph[cur]:
        finish_time[nxt] = max(finish_time[nxt], finish_time[cur] + t[nxt])

        indegree[nxt] -= 1

        if indegree[nxt] == 0:
            q.append(nxt)

for f_time in finish_time:
    print(f_time)