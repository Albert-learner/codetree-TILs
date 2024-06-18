N, M, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
winds = [map(lambda x: int(x) - 1, input().split()) for _ in range(Q)]

def rotate_border(x1, y1, x2, y2):
    tmp = board[x1][y1]

    for i in range(x1, x2):
        board[i][y1] = board[i + 1][y1]

    for i in range(y1, y2):
        board[x2][i] = board[x2][i + 1]

    for i in range(x2, x1, -1):
        board[i][y2] = board[i - 1][y2]

    for i in range(y2, y1, -1):
        board[x1][i] = board[x1][i - 1]

    board[x1][y1 + 1] = tmp

def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def surround_avg(board, x, y):
    sum_cst = board[x][y]
    cnts = 1

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        mx, my = x + dx, y + dy
        if not in_range(mx, my):
            continue

        sum_cst += board[mx][my]
        cnts += 1

    return int(sum_cst / cnts)

for x1, y1, x2, y2 in winds:
    x3, y3, x4, y4 = x1, y1, x2, y2

    rotate_border(x1, y1, x2, y2)

    new_board = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            new_board[i][j] = board[i][j]

    for x in range(x3, x4 + 1):
        for y in range(y3, y4 + 1):
            board[x][y] = surround_avg(new_board, x, y)

for row in board:
    print(*row)