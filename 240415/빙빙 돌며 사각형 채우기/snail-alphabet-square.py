N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

x, y = 0, 0
move_chr = 'A'
move_dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}
dir_num = 0

for _ in range(N * M):
    board[x][y] = move_chr

    mx, my = x + move_dirs[dir_num][0], y + move_dirs[dir_num][1]
    if mx < 0 or mx >= N or my < 0 or my >= M or board[mx][my] != 0:
        dir_num = (dir_num + 1) % 4

    x += move_dirs[dir_num][0]
    y += move_dirs[dir_num][1]
    move_chr = chr(ord(move_chr) + 1)

for row in board:
    print(*row)