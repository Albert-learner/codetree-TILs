board = [list(map(int, input().split())) for _ in range(4)]

areas = 0
for i in range(len(board)):
    for j in range(len(board[0])):
        if i >= j:
            areas += board[i][j]

print(areas)