board = [list(map(int, input().split())) for _ in range(19)]

winner = 0
mid_coord = None

move_dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1)]
def DFS(x, y, cnts, color, dx, dy):
    global winner, mid_coord

    if cnts == 5:
        winner = color
        mid_coord = (x - dx * 2, y - dy * 2)
        return
    
    mx, my = x + dx, y + dy
    if 0 <= mx < 19 and 0 <= my < 19 and board[mx][my] == color:
        DFS(mx, my, cnts + 1, color, dx, dy)
    else:
        return

for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] == 1 or board[i][j] == 2:
            for dx, dy in move_dirs:
                DFS(i, j, 1, board[i][j], dx, dy)

if winner != 0:
    print(winner)
    print(mid_coord[0] + 1, mid_coord[1] + 1)
else:
    print(0)