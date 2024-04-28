x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

board = [[0] * 101 for _ in range(101)]

for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        board[i][j] += 1

for i in range(a1, a2 + 1):
    for j in range(b1, b2 + 1):
        board[i][j] += 1

confirm = False
for row in range(len(board)):
    for col in range(len(board[0])):
        if board[row][col] >= 2:
            confirm = True
            break

if confirm:
    print("overlapping")
else:
    print("nonoverlapping")