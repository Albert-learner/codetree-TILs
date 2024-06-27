N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
bombs = [int(input()) - 1 for _ in range(M)]

def in_range(row, col):
    if row < 0 or N <= row:
        return False
    if col < 0 or N <= col:
        return False

    return True

def explode(row, col):
    len_bomb = board[row][col]
    board[row][col] = 0

    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        tr, tc = row, col
        for _ in range(len_bomb - 1):
            mr, mc = tr + dr, tc + dc

            if not in_range(mr, mc):
                break

            board[mr][mc] = 0

            tr, tc = mr, mc
    fall()

def fall():
    for col in range(N):
        tmp = []
        for i in range(N - 1, -1, -1):
            num = board[i][col]
            if num:
                tmp.insert(0, num)
        while len(tmp) < N:
            tmp.insert(0, 0)

        for i in range(N):
            board[i][col] = tmp[i]

for bomb_col in bombs:
    for row in range(N):
        if board[row][bomb_col]:
            explode(row, bomb_col)
            break

for row in board:
    print(*row)