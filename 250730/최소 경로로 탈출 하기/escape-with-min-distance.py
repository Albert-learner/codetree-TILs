n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

visited = [[False] * m for _ in range(n)]
dists = [[-1] * m for _ in range(n)]

def BFS():
    while que:
        x, y = que.popleft()

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            mx, my = x + dx, y + dy

            if 0 <= mx < n and 0 <= my < m and a[mx][my] == 1 and not visited[mx][my]:
                visited[mx][my] = True
                dists[mx][my] = dists[x][y] + 1
                que.append((mx, my))

que = deque()
visited[0][0] = True
dists[0][0] = 0
que.append((0, 0))

BFS()

print(dists[n - 1][m - 1])