n, m, t = map(int, input().split())

mapper = {
    "U" : 0,
    "L" : 1,
    "R" : 2,
    "D" : 3
}

board = [[-1] * n for _ in range(n)]
marbles = []
for idx in range(1, m + 1):
    ri, ci, di, wi = input().split()
    ri, ci = int(ri) - 1, int(ci) - 1
    marbles.append((ri, ci, mapper[di], int(wi), idx))

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(marble):
    x, y, d, w, idx = marble
    dxs, dys = [-1, 0, 0, 1], [0, -1, 1, 0]

    nxt_x, nxt_y = x + dxs[d], y + dys[d]
    nxt_d = d

    if not in_range(nxt_x, nxt_y):
        nxt_d = 3 - d
        nxt_x, nxt_y = x, y

    return nxt_x, nxt_y, nxt_d, w, idx

def move_all(marbles):
    new_board = [[-1] * n for _ in range(n)]
    nxt_marbles = []

    for marble in marbles:
        x, y, d, w, idx = move(marble)

        if new_board[x][y] == -1:
            new_board[x][y] = len(nxt_marbles)
            nxt_marbles.append((x, y, d, w, idx))
        else:
            other_idx = new_board[x][y]
            ox, oy, od, ow, oidx = nxt_marbles[other_idx]

            # 병합 규칙
            total_w = w + ow
            new_d = d if idx > oidx else od
            new_idx = idx if idx > oidx else oidx

            nxt_marbles[other_idx] = (x, y, new_d, total_w, new_idx)

    return nxt_marbles


def simulate(marbles, t):
    for _ in range(t):
        marbles = move_all(marbles)

    return marbles

marbles = simulate(marbles, t)

marbles.sort(key = lambda x: x[3])
print(len(marbles), marbles[-1][3])