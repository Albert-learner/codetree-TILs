moves = input()
dir_num = 0

move_dirs = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

x, y = 0, 0
answer, times = 0, 0
for move in moves:
    if move == 'L':
        dir_num = (dir_num + 3) % 4 
    elif move == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + move_dirs[dir_num][0], y + move_dirs[dir_num][1]
        if (x, y) == (0, 0):
            times += 1
            answer += times
            break

    if (x, y) == (0, 0):
        break

    times += 1

print(answer)