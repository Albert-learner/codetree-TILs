N, M = map(int, input().split())
first_board = [list(map(int, input().split())) for _ in range(N)]
second_board = [list(map(int, input().split())) for _ in range(N)]

confirm = [[0] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if first_board[i][j] != second_board[i][j]:
            confirm[i][j] = 1

for row in confirm:
    print(*row)