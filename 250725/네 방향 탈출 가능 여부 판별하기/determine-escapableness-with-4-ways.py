n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

visited = [[False] * m for _ in range(n)]

def BFS():
    while que:
        x, y = que.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and a[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                que.append((nx, ny))

que = deque()
visited[0][0] = True
que.append((0, 0))

BFS()

print(1 if visited[n - 1][m - 1] == True else 0)