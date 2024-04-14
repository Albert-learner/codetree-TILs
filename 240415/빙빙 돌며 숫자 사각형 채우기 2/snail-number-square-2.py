N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

move_dirs = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
x, y = 0, 0
num = 1
dir_num = 0

for _ in range(N * M):
    board[x][y] = num

    mx, my = x + move_dirs[dir_num][0], y + move_dirs[dir_num][1]
    if mx < 0 or mx >= N or my < 0 or my >= M or board[mx][my] != 0:
        dir_num = (dir_num + 1) % 4

    x += move_dirs[dir_num][0]
    y += move_dirs[dir_num][1]
    num += 1

for row in board:
    print(*row)