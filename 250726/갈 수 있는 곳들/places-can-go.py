n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
from collections import deque

visited = [[False] * n for _ in range(n)]
que = deque()

for x, y in points:
    rx, ry = x - 1, y - 1

    que.append((rx, ry))
    visited[rx][ry] = True

    while que:
        x, y = que.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            mx, my = x + dx, y + dy

            if 0 <= mx < n and 0 <= my < n and grid[mx][my] == 0 and not visited[mx][my]:
                visited[mx][my] = True
                que.append((mx, my))

possibles = 0
for row in visited:
    possibles += row.count(True)

print(possibles)