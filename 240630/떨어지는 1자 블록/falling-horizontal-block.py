N, M, K = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
flag = False

for row in range(N):
    for col in range(K - 1, K - 1 + M):
        if board[row][col] == 1:
            for j in range(K - 1, K - 1 + M):
                board[row - 1][j] = 1
            flag = True
            break
    if flag:
        break
        
if not flag:
    for row in range(N):
        for col in range(K - 1,K - 1 + M):
            board[row][col] = 1

for row in board:
    print(*row)