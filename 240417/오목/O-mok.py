board = [list(map(int, input().split())) for _ in range(19)]

winner = 0
mid_coord = None

# 상, 우상, 우, 우하
dx = [-1, -1, 0, 1]
dy = [0, 1, 1, 1]

def DFS(x, y, cnt, color, f_dir):
    global winner, mid_coord

    if cnt == 5:
        winner = color
        mid_coord = (x - dx[f_dir] * 2, y - dy[f_dir] * 2)
        return

    mx, my = x + dx[f_dir], y + dy[f_dir]
    if 0 <= mx < 19 and 0 <= my < 19 and board[mx][my] == color:
        DFS(mx, my, cnt + 1, color, f_dir)
    else:
        return

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 1 or board[i][j] == 2:
            for k in range(4):
                DFS(i, j, 1, board[i][j], k)

if winner != 0:
    print(winner)
    print(mid_coord[0] + 1, mid_coord[1] + 1)
else:
    print(0)