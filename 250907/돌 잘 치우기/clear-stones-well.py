n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

starts = []
for _ in range(k):
    ri, ci = map(int, input().split())
    starts.append((ri - 1, ci - 1))

# Please write your code here.
from collections import deque
from itertools import combinations

stones = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def reachable_count(removed_set):
    q = deque()
    visited = [[False] * n for _ in range(n)]

    for sx, sy in starts:
        if not visited[sx][sy]:
            visited[sx][sy] = True
            q.append((sx, sy))

    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny) or visited[nx][ny]:
                continue

            if grid[nx][ny] == 0 or (nx, ny) in removed_set:
                visited[nx][ny] = True
                q.append((nx, ny))
    return cnt

best = 0
if m == 0:
    best = reachable_count(set())
else:
    for comb in combinations(stones, m):
        best = max(best, reachable_count(set(comb)))

print(best)
