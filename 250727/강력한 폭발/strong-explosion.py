n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
bomb_type = [
    [0 for _ in range(n)]
    for _ in range(n)
]
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]
pts = []
max_cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            pts.append([i, j])

def count():
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                visited[i][j] = False
    for i in range(n):
        for j in range(n):
            if bomb_type[i][j]:
                fill_grid(i, j, bomb_type[i][j])
    # print_visited()
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1

    global max_cnt
    max_cnt = max(max_cnt, cnt)


def in_range(i, j):
    return 0 <= i < n and 0 <= j < n

def choose(n):
    if n == len(pts):
        count()
        return
    for i in range(1, 4):
        x, y = pts[n]
        bomb_type[x][y] = i
        choose(n + 1)
        bomb_type[x][y] = 0


def fill_grid(i, j, k):
    if k == 1:
            dis, djs = [-2, -1, 1, 2], [0, 0, 0, 0]
    if k == 2:
            dis, djs = [-1, 1, 0, 0], [0, 0, -1, 1]
    if k == 3:
            dis, djs = [-1, -1, 1, 1], [-1, 1, -1, 1]
    visited[i][j] = True
    for di, dj in zip(dis, djs):
        new_i, new_j = i + di, j + dj
        if in_range(new_i, new_j):
            visited[new_i][new_j] = True

choose(0)

print(max_cnt)