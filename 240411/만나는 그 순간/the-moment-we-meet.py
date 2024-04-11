N, M = map(int, input().split())
n_moves, m_moves = [], []

for _ in range(N):
    mv_dir, size = input().split()
    size = int(size)
    n_moves.append([mv_dir, size])

for _ in range(M):
    mv_dir, size = input().split()
    size = int(size)
    m_moves.append([mv_dir, size])

cur_a, cur_b = 0, 0
a, b = [], []
for mv_dir, size in n_moves:
    if mv_dir == 'R':
        for i in range(cur_a, cur_a + size):
            a.append(i)
        cur_a += size
    else:
        for i in range(cur_a, cur_a - size, -1):
            a.append(i)
        cur_a -= size

for mv_dir, size in m_moves:
    if mv_dir == 'R':
        for i in range(cur_b, cur_b + size):
            b.append(i)
        cur_b += size
    else:
        for i in range(cur_b, cur_b - size, -1):
            b.append(i)
        cur_b -= size

a, b = a[1:], b[1:]
answer, idx = -1, 0
for a_elem, b_elem in zip(a, b):
    if a_elem == b_elem:
        idx += 1
        answer = idx
        break

    idx += 1
print(answer)