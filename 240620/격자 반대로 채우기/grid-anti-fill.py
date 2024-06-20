N = int(input())
board = [[0] * N for _ in range(N)]

num = 0
if N % 2 == 0:
    for j in range(N - 1, -1, -1):
        if j % 2 == 1:
            for i in range(N - 1, -1, -1):
                num += 1
                board[i][j] = num
        else:
            for i in range(N):
                num += 1
                board[i][j] = num
else:
    for j in range(N - 1, -1, -1):
        if j % 2 == 0:
            for i in range(N - 1, -1, -1):
                num += 1
                board[i][j] = num
        else:
            for i in range(N):
                num += 1
                board[i][j] = num

for row in board:
    print(*row)