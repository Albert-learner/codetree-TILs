N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
move_dirs = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}

cnts, answer = 0, 0
for i in range(len(board)):
    for j in range(len(board[0])):
        four_coords = [(i + dx, j + dy) for dx, dy in move_dirs.values() if
                       (i + dx) in range(N) and (j + dy) in range(N)]
        for mx, my in four_coords:
            if board[mx][my] == 1:
                cnts += 1

        if cnts >= 3:
            answer += 1
            cnts = 0
        cnts = 0
    cnts = 0

print(answer)