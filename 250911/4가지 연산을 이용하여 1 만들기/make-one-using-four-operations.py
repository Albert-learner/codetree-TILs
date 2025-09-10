N = int(input())

# Please write your code here.
from collections import deque

max_val = max(2 * N, 2)

visited = [False] * (max_val + 1)
q = deque([(N, 0)])
visited[N] = True

while q:
    x, d = q.popleft()
    if x == 1:
        print(d)
        break

    nxts = []
    if x - 1 >= 1:
        nxts.append(x - 1)
    if x + 1 <= max_val:
        nxts.append(x + 1)
    if x % 2 == 0:
        nxts.append(x // 2)
    if x % 3 == 0:
        nxts.append(x // 3)

    for nxt in nxts:
        if not visited[nxt]:
            visited[nxt] = True
            q.append((nxt, d + 1))