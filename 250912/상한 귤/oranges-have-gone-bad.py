n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

res = [[0] * n for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            res[i][j] = -1
        elif grid[i][j] == 1:
            res[i][j] = -2
        else:
            res[i][j] = 0
            q.append((i, j))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while q:
    x, y = q.popleft()
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n:
            if grid[nx][ny] == 1 and res[nx][ny] == -2:
                res[nx][ny] = res[x][y] + 1
                q.append((nx, ny))

for row in res:
    print(*row)