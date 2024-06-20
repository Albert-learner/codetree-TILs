N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]

num = 1
ij_sum = 0

while ij_sum <= N * M:
    for i in range(N):
        for j in range(M):
            if i + j == ij_sum:
                board[i][j] = num
                num += 1
            else:
                continue

    ij_sum += 1

for row in board:
    print(*row)