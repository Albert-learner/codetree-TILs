N, M, K = tuple(map(int, input().split()))
K -= 1
board = [list(map(int, input().split())) for _ in range(N)]

def down(board, n, m, k):
    row = get_row_position(board, n, m, k)

    for j in range(k, k + m):
        board[row][j] = 1

def get_row_position(board, n, m, k):
    for i in range(n - 1):
        is_up_blank = all(board[i][j] == 0 for j in range(k, k + m))
        is_down_blank = all(board[i + 1][j] == 0 for j in range(k, k + m))

        if is_up_blank and not is_down_blank:
            return i

    return n - 1

down(board, N, M, K)

for row in board:
    print(*row)