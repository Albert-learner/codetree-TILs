N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
r, c, m1, m2, m3, m4, t_dir = map(int, input().split())

dx = [-1, -1, 1, 1]
cntr_dy = [1, -1, -1, 1]
clock_dy = [-1, 1, 1, -1]
dy = cntr_dy if t_dir == 0 else clock_dy

steps = [m1 if t_dir == 0 else m2, m2 if t_dir == 0 else m1]

cnts = 0
d = 0
prev = 0
x, y = r - 1, c - 1

while cnts < ((m1 + 1) * 2) + ((m2 - 1) * 2):
    ting_dir = d % 4
    for s in range(steps[ting_dir % 2]):
        tmp = board[x][y]
        if prev > 0:
            board[x][y] = prev
            cnts += 1
            if cnts == ((m1 + 1) * 2) + ((m2 - 1) * 2):
                break

        x, y = x + dx[ting_dir], y + dy[ting_dir]
        prev = tmp

    d += 1

for row in board:
    print(*row)