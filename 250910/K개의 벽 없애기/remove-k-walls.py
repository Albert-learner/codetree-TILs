n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

# Please write your code here.
from collections import deque
from itertools import combinations

walls = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(removed):
    dists = [[-1] * n for _ in range(n)]
    q = deque()
    dists[r1][c1] = 0
    q.append((r1, c1))

    while q:
        x, y = q.popleft()
        if (x, y) == (r2, c2):
            return dists[x][y]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or dists[nx][ny] != -1:
                continue

            if grid[nx][ny] == 0 or (nx, ny) in removed:
                dists[nx][ny] = dists[x][y] + 1
                q.append((nx, ny))

    return -1

min_times = float("inf")
if k == 0:
    d = bfs(set())
    if d != -1:
        min_times = min(min_times, d)
else:
    for comb in combinations(walls, k):
        d = bfs(set(comb))
        if d != -1 and d < min_times:
            min_times = d

print(min_times if min_times != float("inf") else -1)