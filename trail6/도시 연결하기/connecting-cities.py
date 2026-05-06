n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

city = [[0] * m for _ in range(n)]
city_id = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 1 and city[i][j] == 0:
            city_id += 1
            q = deque()
            q.append((i, j))
            city[i][j] = city_id

            while q:
                r, c = q.popleft()

                for d in range(4):
                    nr = r + dr[d]
                    nc = c + dc[d]

                    if 0 <= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == 1 and city[nr][nc] == 0:
                            city[nr][nc] = city_id
                            q.append((nr, nc))

edges = []

for r in range(n):
    c = 0
    while c < m:
        if city[r][c] == 0:
            c += 1
            continue

        start = city[r][c]
        nc = c + 1
        length = 0

        while nc < m and city[r][nc] == 0:
            length += 1
            nc += 1

        if nc < m:
            end = city[r][nc]
            if start != end and length > 0:
                edges.append((length, start, end))

        c += 1

for c in range(m):
    r = 0
    while r < n:
        if city[r][c] == 0:
            r += 1
            continue

        start = city[r][c]
        nr = r + 1
        length = 0

        while nr < n and city[nr][c] == 0:
            length += 1
            nr += 1

        if nr < n:
            end = city[nr][c]
            if start != end and length > 0:
                edges.append((length, start, end))

        r += 1

parent = list(range(city_id + 1))

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
used = 0

for cost, a, b in edges:
    if union(a, b):
        answer += cost
        used += 1

        if used == city_id - 1:
            break

if used == city_id - 1:
    print(answer)
else:
    print(-1)