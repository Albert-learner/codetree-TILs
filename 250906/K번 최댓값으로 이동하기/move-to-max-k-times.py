n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# Please write your code here.
from collections import deque

r -= 1
c -= 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def choose_next(x, y):
    limit = grid[x][y]
    q = deque()
    visited = [[False]*n for _ in range(n)]

    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] < limit and not visited[nx][ny]:
            visited[nx][ny] = True
            q.append((nx, ny))


    best = None

    while q:
        cx, cy = q.popleft()
        val = grid[cx][cy]

        if best is None:
            best = (val, cx, cy)
        else:
            bv, br, bc = best
            if (val > bv) or (val == bv and (cx < br or (cx == br and cy < bc))):
                best = (val, cx, cy)

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = cx + dx, cy + dy
            if in_range(nx, ny) and not visited[nx][ny] and grid[nx][ny] < limit:
                visited[nx][ny] = True
                q.append((nx, ny))

    if best is None:
        return None
    else:
        return (best[1], best[2])

for _ in range(k):
    nxt = choose_next(r, c)
    if nxt is None:
        break
    r, c = nxt

print(r + 1, c + 1)