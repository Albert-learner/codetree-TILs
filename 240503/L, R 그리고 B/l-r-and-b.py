grids = [list(input()) for _ in range(10)]

start_x, start_y, target_x, target_y, disturb_x, disturb_y = 0, 0, 0, 0, 0, 0
for row in range(10):
    for col in range(10):
        if grids[row][col] == 'L':
            start_x, start_y = row, col
        elif grids[row][col] == 'B':
            target_x, target_y = row, col
        elif grids[row][col] == 'R':
            disturb_x, disturb_y = row, col

routes_pos = []
min_dists = 0
sx, sy, tx, ty = start_x, start_y, target_x, target_y
if tx < sx and ty < sy:
    sx, sy, tx, ty = tx, ty, sx, sy

while sx != tx and sy != ty:
    sy += 1
    routes_pos.append((sx, sy))
    sx += 1
    routes_pos.append((sx, sy))

if (disturb_x, disturb_y) in routes_pos:
    min_dists += 1

min_dists = abs(target_x - start_x) + abs(target_y - start_y) - 1
print(min_dists)