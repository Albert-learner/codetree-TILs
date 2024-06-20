N, M = map(int, input().split())
poses = [map(lambda x: int(x) - 1, input().split()) for _ in range(M)]

board = [[0] * N for _ in range(N)]
for idx, (x, y) in enumerate(poses, 1):
    board[x][y] = idx

for row in board:
    print(*row)