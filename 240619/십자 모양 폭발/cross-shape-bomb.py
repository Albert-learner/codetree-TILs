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

# # 모범답안
# # 변수 선언 및 입력:

# n = int(input())
# grid = [
#     list(map(int, input().split()))
#     for _ in range(n)
# ]
# next_grid = [
#     [0 for _ in range(n)]
#     for _ in range(n)
# ]


# def in_bomb_range(x, y, center_x, center_y, bomb_range):
#     return (x == center_x or y == center_y) and \
#            abs(x - center_x) + abs(y - center_y) < bomb_range


# def bomb(center_x, center_y):
#     bomb_range = grid[center_x][center_y]
    
#     # Step1. 폭탄이 터질 위치는 0으로 채워줍니다.
#     for i in range(n):
#         for j in range(n):
#             if in_bomb_range(i, j, center_x, center_y, bomb_range):
#                 grid[i][j] = 0
	
#     # Step2. 폭탄이 터진 이후의 결과를 next_grid에 저장합니다.
#     for j in range(n):
#         next_row = n - 1
#         for i in range(n - 1, -1, -1):
#             if grid[i][j]:
#                 next_grid[next_row][j] = grid[i][j]
#                 next_row -= 1
                
#     # Step3. grid로 다시 값을 옮겨줍니다.
#     for i in range(n):
#         for j in range(n):
#             grid[i][j] = next_grid[i][j]

            
# r, c = tuple(map(int, input().split()))
# bomb(r - 1, c - 1)

# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end=" ")
#     print()

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