N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def rotate_90_clockwise(board):
    return [list(row) for row in zip(*board[::-1])]

def make_zero(board, sr, er, col):
    for i in range(sr, er + 1):
        board[i][col] = 0

def explode(board, n, m):
    is_bombed = False
    for j in range(n):
        cur_num = board[0][j]
        cur_cnts, start_idx = 1, 0
        for i in range(1, n):
            if board[i][j] == 0:
                continue
            if cur_num == board[i][j]:
                cur_cnts += 1
            else:
                if cur_cnts >= m:
                    is_bombed = True
                    make_zero(board, start_idx, i - 1, j)
                cur_num = board[i][j]
                cur_cnts = 1
                start_idx = i
        if cur_cnts >= m and cur_num != 0:
            is_bombed = True
            make_zero(board, start_idx, n - 1, j)

    return is_bombed

def initialize_new_board(n):
    return [[0] * n for _ in range(n)]

def apply_gravity(board, n):
    new_board = initialize_new_board(n)
    for j in range(n):
        tmp_last_idx = n - 1
        for i in range(n - 1, -1, -1):
            if board[i][j]:
                new_board[tmp_last_idx][j] = board[i][j]
                tmp_last_idx -= 1

    return new_board

def find_straight_numbers(board, n, m):
    is_bombed = False
    while True:
        is_bombed = explode(board, n, m)
        if is_bombed:
            board = apply_gravity(board, n)
            is_bombed = False
        else:
            board = apply_gravity(board, n)
            break

    return board

while K > 0:
    board = find_straight_numbers(board, N, M)
    board = rotate_90_clockwise(board)
    board = find_straight_numbers(board, N, M)
    K -= 1

answer = sum(1 for i in range(N) for j in range(N) if board[i][j] != 0)
print(answer)