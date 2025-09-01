n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def has_run(seq, m_cnts):
    run = 1

    for i in range(1, len(seq)):
        if seq[i - 1] == seq[i]:
            run += 1
            if run >= m_cnts:
                return True
        else:
            run = 1

    return False if run < m_cnts else True

happy_seqs = 0

for row in grid:
    if has_run(row, m):
        happy_seqs += 1

for c_idx in range(n):
    col = [grid[r_idx][c_idx] for r_idx in range(n)]
    if has_run(col, m):
        happy_seqs += 1

print(happy_seqs)