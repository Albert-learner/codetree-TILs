N, M = map(int, input().split())
board = [[0] * N for _ in range(N)]
chk_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(M):
    r, c = map(lambda x: int(x) - 1, input().split())
    board[r][c] = 1

    colors = 0
    for dr, dc in chk_dirs:
        mr, mc = r + dr, c + dc
        if 0 <= mr < N and 0 <= mc < N and board[mr][mc] == 1:
            colors += 1

    print(1 if colors == 3 else 0)