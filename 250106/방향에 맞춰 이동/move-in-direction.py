n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dirs = [move[0] for move in moves]
dists = [int(move[1]) for move in moves]

# Write your code here!
mx, my = 0, 0
m_dir_info = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
for m_dir, m_dst in zip(dirs, dists):
    mx += m_dir_info[m_dir][0] * m_dst
    my += m_dir_info[m_dir][1] * m_dst

print(mx, my)
