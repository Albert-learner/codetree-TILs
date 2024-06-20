N = int(input())
board = [[0] * N for _ in range(N)]

num = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        num += 1
        board[j][i] = num

for row in board:
    print(*row)