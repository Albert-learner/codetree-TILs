def DFS(board, x, y, cnts, color, dx, dy):
    if cnts == 5:
        return color, (x - dx * 2, y - dy * 2)
    
    mx, my = x + dx, y + dy
    if 0 <= mx < 19 and 0 <= my < 19 and board[mx][my] == color:
        return DFS(board, mx, my, cnts + 1, color, dx, dy)
    else:
        return None

def find_winner(board):
    move_dirs = [(-1, 0), (-1, 1), (0, 1), (1, 1)]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1 or board[i][j] == 2:
                for dx, dy in move_dirs:
                    result = DFS(board, i, j, 1, board[i][j], dx, dy)
                    if result:
                        return result
    return 0, None

board = [list(map(int, input().split())) for _ in range(19)]
winner, mid_coord = find_winner(board)

if winner != 0:
    print(winner)
    print(mid_coord[0] + 1, mid_coord[1] + 1)
else:
    print(0)