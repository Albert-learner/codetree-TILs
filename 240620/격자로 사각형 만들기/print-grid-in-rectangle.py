N = int(input())
board = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 or j == 0:
            board[i][j] = 1

for i in range(1, N):
    for j in range(1, N):
        board[i][j] = board[i - 1][j - 1] + board[i][j - 1] + board[i - 1][j]

for row in board:
    print(*row)