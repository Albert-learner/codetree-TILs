N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_cnts = 0
for i in range(N):
    for j in range(N - 2):
        max_cnts = max(max_cnts, board[i][j] + board[i][j + 1] + board[i][j + 2])

print(max_cnts)