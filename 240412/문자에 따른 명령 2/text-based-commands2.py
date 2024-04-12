moves = input()

x, y = 0, 0
dir_num = 3
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]

for move in moves:
    if move == 'L':
        dir_num = (dir_num - 1 + 4) % 4
    elif move == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x, y = x + dx[dir_num], y + dy[dir_num]

print(x, y)