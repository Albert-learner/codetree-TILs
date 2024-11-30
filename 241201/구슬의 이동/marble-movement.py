from collections import defaultdict

def in_range(r, c, n):
    return 0 <= r < n and 0 <= c < n

def move(i, r, c, d, v, n):
    dr_dcs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(v):
        nr, nc = r + dr_dcs[d][0], c + dr_dcs[d][1]

        if not in_range(nr, nc, n):
            d = d ^ 1
            nr, nc = nr + dr_dcs[d][0] * 2, nc + dr_dcs[d][1] * 2

        r, c = nr, nc

    return [i, r, c, d, v]

def move_all(beads, n):
    tmp = []

    for info in beads:
        tmp.append(move(*info, n))

    return tmp

def remove_duplicate_beads(beads, k):
    beads_dict = defaultdict(list)

    tmp = []
    for info in beads:
        i, r, c, d, v = info
        beads_dict[(r, c)].append(info)

    for infos in beads_dict.values():
        if len(infos) <= k:
            tmp.extend(infos)
        else:
            tmp.extend(sorted(infos, key = lambda x: (-x[4], -x[0]))[:k])

    return tmp

def simulate(beads, n, k):
    beads = move_all(beads, n)
    beads = remove_duplicate_beads(beads, k)

    return beads

mapper = {'U': 0, 'D': 1, 'L': 2, 'R': 3}
N, M, T, K = map(int, input().split())

beads = []
for i in range(1, M + 1):
    r, c, d, v = input().split()
    r_int, c_int, d_int, v_int = int(r) - 1, int(c) - 1, mapper[d], int(v)
    beads.append([i, r_int, c_int, d_int, v_int])

for _ in range(T):
    beads = simulate(beads, N, K)

print(len(beads))


