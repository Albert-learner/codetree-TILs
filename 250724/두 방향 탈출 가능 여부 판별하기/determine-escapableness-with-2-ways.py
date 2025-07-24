n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
routes = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def check_possible(x, y):
    if not in_range(x, y):
        return False

    if grid[x][y] == 0 or visited[x][y]:
        return False

    return True

def DFS(x, y):
    global order
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if check_possible(nx, ny):
            routes[nx][ny] = order
            order += 1
            visited[nx][ny] = True
            DFS(nx, ny)

order = 0
routes[0][0] = 0
order += 1
DFS(0, 0)

if routes[n - 1][m - 1] != 0:
    print(1)
else:
    print(0)