N, M, R, C = map(int, input().split())
roll_dirs = input().split()

R, C = R - 1, C - 1
board = [[0] * N for _ in range(N)]

d_coords_dict = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
}

dice = [
    [0, 5, 0],
    [4, 6, 3],
    [0, 2, 0]
]

def sum_board():
    return sum(map(sum, board))

def in_range(r, c):
    return 0 <= r < N and 0 <= c < N

def cur_eyes():
    return dice[1][1]

def roll(dce):
    if dce == 'L':
        dice[1] = [7 - cur_eyes(), dice[1][0], dice[1][1]]
    if dce == 'R':
        dice[1] = [dice[1][1], dice[1][2], 7 - cur_eyes()]
    if dce == 'U':
        [dice[0][1], dice[1][1], dice[2][1]] = [7 - cur_eyes(), dice[0][1], dice[1][1]]
    if dce == 'D':
        [dice[0][1], dice[1][1], dice[2][1]] = [dice[1][1], dice[2][1], 7 - cur_eyes()]

board[R][C] = cur_eyes()

for roll_dce in roll_dirs:
    dr, dc = d_coords_dict[roll_dce]

    mr, mc = R + dr, C + dc

    if not in_range(mr, mc):
        continue

    R, C = mr, mc
    roll(roll_dce)
    board[R][C] = cur_eyes()

print(sum_board())