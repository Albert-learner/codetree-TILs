n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def ok(x1, y1, x2, y2):
    diff = abs(grid[x1][y1] - grid[x2][y2])
    return u <= diff <= d

visited = [[False] * n for _ in range(n)]
sizes = []

dirs = [(-1, 0),(1, 0),(0, -1),(0, 1)]

for i in range(n):
    for j in range(n):
        if visited[i][j]:
            continue
        q = deque([(i, j)])
        visited[i][j] = True
        cnt = 0
        while q:
            x, y = q.popleft()
            cnt += 1
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and not visited[nx][ny] and ok(x, y, nx, ny):
                    visited[nx][ny] = True
                    q.append((nx, ny))
        sizes.append(cnt)


sizes.sort(reverse = True)
answer = sum(sizes[:min(k, len(sizes))])
print(answer)