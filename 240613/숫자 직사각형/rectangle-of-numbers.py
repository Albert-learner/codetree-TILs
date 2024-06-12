N, M = map(int, input().split())

board = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(1, M + 1):
        board[i][j - 1] = i * M + j

for row in board:
    print(*row)