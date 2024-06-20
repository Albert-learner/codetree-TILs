board = [[1] * 5 for _ in range(5)]

for i in range(1, 5):
    for j in range(1, 5):
        board[i][j] = board[i - 1][j] + board[i][j - 1]

for row in board:
    print(*row)