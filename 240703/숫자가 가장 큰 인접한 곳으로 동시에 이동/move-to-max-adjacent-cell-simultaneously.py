N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
marble_poses = [map(lambda x: int(x) - 1, input().split()) for _ in range(M)]

counts = [[0] * N for _ in range(N)]
for x, y in marble_poses:
    counts[x][y] = 1

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def next_pos(x, y):
    max_num = 0
    max_pos = (-1, -1)

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        mx, my = x + dx, y + dy
        if in_range(mx, my) and board[mx][my] > max_num:
            max_num = board[mx][my]
            max_pos = (mx, my)

    x, y = max_pos

    return x, y

def simulate(cnts):
    tmp_counts = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if cnts[i][j] == 1:
                x, y = next_pos(i, j)
                tmp_counts[x][y] += 1

    return tmp_counts

def boom(cnts):
    for i in range(N):
        for j in range(N):
            if cnts[i][j] >= 2:
                cnts[i][j] = 0

    return cnts

for _ in range(T):
    cnts = simulate(counts)
    cnts = boom(cnts)

totals = 0
for i in range(N):
    for j in range(N):
        totals += cnts[i][j]

print(totals)