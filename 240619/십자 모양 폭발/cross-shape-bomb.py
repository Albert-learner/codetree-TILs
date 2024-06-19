N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
R, C = map(lambda x: int(x) - 1, input().split())

def in_range(r, c, n):
    return 0 <= r < n and 0 <= c < n

def bomb(board, n, r, c):
    len_bomb = board[r][c] - 1
    board[r][c] = 0

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in directions:
        mr, mc = r, c
        for _ in range(len_bomb):
            mr += dr
            mc += dc
            if not in_range(mr, mc, n):
                break

            board[mr][mc] = 0

def fall(board, n):
    tmp = [[0] * n for _ in range(n)]
    for c in range(n):
        idx = n - 1
        for r in range(n - 1, -1, -1):
            if board[r][c] != 0:
                tmp[idx][c] = board[r][c]
                idx -= 1

    return tmp

def process(board, n, r, c):
    bomb(board, n, r, c)

    return fall(board, n)

board = process(board, N, R, C)
for row in board:
    print(*row)

# 내 풀이
# N = int(input())
# board = [input().split() for _ in range(N)]
# r, c = map(lambda x: int(x) - 1, input().split())

# if board[r][c] == '1':
#     rm_col = [row[c] for row in board]
#     rm_col.pop(r)
#     for i in range(len(board)):
#         board[i][c] = ' '

#     for i, rm in zip(range(len(board) - 1, 0, -1), rm_col):
#         board[i][c] = rm
# else:
#     diff = int(board[r][c]) - 1
#     rm_col_idxs = [c - 1, c, c + 1] if c - 1 >= 0 and c + 1 < N else [c, c + 1] if c == 0 else [c - 1, c]
#     rm_cols = [[row[rm_col_idx] for row in board] for rm_col_idx in rm_col_idxs]
    
#     for i in range(len(board)):
#         for rm_col_idx in rm_col_idxs:
#             board[i][rm_col_idx] = ' '

#     if len(rm_cols) == 3:
#         for rm_col_idx, rm_col in enumerate(rm_cols, 1):
#             if rm_col_idx != 2:
#                 rm_col.pop(r)
#             else:
                
#         print(rm_cols)
#     else:


# # for row in board:
# #     print(*row)