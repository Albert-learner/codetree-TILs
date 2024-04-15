N, T = map(int, input().split())
commands = input()
board = [list(map(int, input().split())) for _ in range(N)]

move_dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
x, y = len(board) // 2, len(board[0]) // 2
dir_num = 0

answer = board[x][y]
for cmd in commands:
    if cmd == 'R':
        dir_num = (dir_num + 1) % 4
    elif cmd == 'L':
        dir_num = (dir_num + 3) % 4
    else:
        if 0 <= x + move_dirs[dir_num][0] < N and 0 <= y + move_dirs[dir_num][1] < N:
            x += move_dirs[dir_num][0]
            y += move_dirs[dir_num][1]
            answer += board[x][y]
        else:
            continue

print(answer)