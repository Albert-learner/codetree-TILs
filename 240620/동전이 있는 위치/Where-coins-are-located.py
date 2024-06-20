N, M = map(int, input().split())
poses = [map(lambda x: int(x) - 1, input().split()) for _ in range(M)]

board = [[0] * N for _ in range(N)]
for x, y in poses:
    board[x][y] = 1

for row in board:
    print(*row)