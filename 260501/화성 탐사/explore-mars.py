n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

bases = []
start_idx = -1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            start_idx = len(bases)
            bases.append((i, j))
        elif grid[i][j] == 2:
            bases.append((i, j))

base_count = len(bases)

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(sx, sy):
    dist = [[-1] * n for _ in range(n)]
    q = deque()
    q.append((sx, sy))
    dist[sx][sy] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy

            if 0 <= nx < n and 0 <= ny < n:
                if grid[nx][ny] != -1 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    return dist

edges = []
for i in range(base_count):
    sx, sy = bases[i]
    dist = bfs(sx, sy)

    for j in range(i + 1, base_count):
        tx, ty = bases[j]

        if dist[tx][ty] != -1:
            edges.append((dist[tx][ty], i, j))

parent = list(range(base_count))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra = find(a)
    rb = find(b)

    if ra == rb:
        return False

    parent[rb] = ra
    return True

edges.sort()

answer = 0
cnt = 0

for cost, u, v in edges:
    if union(u, v):
        answer += cost
        cnt += 1

        if cnt == base_count - 1:
            break

if cnt == base_count - 1:
    print(answer)
else:
    print(-1)