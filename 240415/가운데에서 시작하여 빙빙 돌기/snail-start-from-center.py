N = int(input())
board = [[0] * N for _ in range(N)]

x, y = len(board) - 1, len(board[0]) - 1
move_dirs = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}
dir_num = 0
num = N ** 2

for _ in range(N * N):
    board[x][y] = num

    mx, my = x + move_dirs[dir_num][0], y + move_dirs[dir_num][1]
    if mx < 0 or mx >= N or my < 0 or my >= N or board[mx][my] != 0:
        dir_num = (dir_num + 1) % 4

    x += move_dirs[dir_num][0]
    y += move_dirs[dir_num][1]
    num -= 1


for row in board:
    print(*row)