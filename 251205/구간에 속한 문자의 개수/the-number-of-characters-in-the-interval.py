n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]

# Read k queries as tuples
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
pa = [[0] * (m + 1) for _ in range(n + 1)]
pb = [[0] * (m + 1) for _ in range(n + 1)]
pc = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    row = grid[i - 1]
    for j in range(1, m + 1):
        ch = row[j - 1]
        pa[i][j] = pa[i - 1][j] + pa[i][j - 1] - pa[i - 1][j - 1]
        pb[i][j] = pb[i - 1][j] + pb[i][j - 1] - pb[i - 1][j - 1]
        pc[i][j] = pc[i - 1][j] + pc[i][j - 1] - pc[i - 1][j - 1]

        if ch == 'a':
            pa[i][j] += 1
        elif ch == 'b':
            pb[i][j] += 1
        elif ch == 'c':
            pc[i][j] += 1

def get_sum(pref, r1, c1, r2, c2):
    return (
        pref[r2][c2]
        - pref[r1 - 1][c2]
        - pref[r2][c1 - 1]
        + pref[r1 - 1][c1 - 1]
    )

for r1, c1, r2, c2 in queries:
    a_cnt = get_sum(pa, r1, c1, r2, c2)
    b_cnt = get_sum(pb, r1, c1, r2, c2)
    c_cnt = get_sum(pc, r1, c1, r2, c2)
    print(a_cnt, b_cnt, c_cnt)