N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

num = 0
for j in range(M):
    if j % 2 == 0:
        for i in range(N):
            board[i][j] = num
            num += 1
    else:
        for i in range(N - 1, -1, -1):
            board[i][j] = num
            num += 1

for row in board:
    print(*row)