import sys

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

def find_pos(num):
    for row in range(N):
        for col in range(N):
            if board[row][col] == num:
                return row, col

def find_max(row, col):
    max_num = -sys.maxsize
    for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
        mx, my = row + dx, col + dy

        if in_range(mx, my):
            if board[mx][my] > max_num:
                max_num = board[mx][my]

    return max_num

def change_board(max_cost, num, row, col):
    max_row, max_col = find_pos(max_cost)

    tmp = board[max_row][max_col]
    board[max_row][max_col] = board[row][col]
    board[row][col] = tmp
    # board[row][col], board[max_row][max_col] = board[max_row][max_col], board[row][col]

    return board

for _ in range(M):
    for n in range(1, N * N + 1):
        r, c = find_pos(n)
        max_cst = find_max(r, c)
        board = change_board(max_cst, n, r, c)

    for row in board:
        print(*row)