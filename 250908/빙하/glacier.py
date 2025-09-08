n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def bfs_outside_water():
    vis = [[False]*m for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in [0, m-1]:
            if a[i][j] == 0 and not vis[i][j]:
                vis[i][j] = True
                q.append((i, j))
    for j in range(m):
        for i in [0, n-1]:
            if a[i][j] == 0 and not vis[i][j]:
                vis[i][j] = True
                q.append((i, j))

    while q:
        x, y = q.popleft()
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not vis[nx][ny] and a[nx][ny] == 0:
                vis[nx][ny] = True
                q.append((nx, ny))
    return vis  

def melt_once():
    outside = bfs_outside_water()
    to_melt = []

    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and outside[ni][nj]:
                        to_melt.append((i, j))
                        break

    for x, y in to_melt:
        a[x][y] = 0
    return len(to_melt)

time = 0
last = 0
total_ice = sum(sum(row) for row in a)

while total_ice > 0:
    melted = melt_once()
    if melted == 0:   
        break
    total_ice -= melted
    time += 1
    last = melted

print(time, last)