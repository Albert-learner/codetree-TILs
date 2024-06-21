N, M = map(int, input().split())
poses = [map(int, input().split()) for _ in range(M)]

board = [[0] * N for _ in range(N)]
for x, y in poses:
    board[x - 1][y - 1] = x * y

for row in board:
    print(*row)