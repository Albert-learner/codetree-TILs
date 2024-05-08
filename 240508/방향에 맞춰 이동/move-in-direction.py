N = int(input())
moves = []
for _ in range(N):
    m_dir, size = input().split()
    moves.append([m_dir, int(size)])

moves_dir = {'N': (0, 1), 'E': (1, 0), 'S': (0, -1), 'W': (-1, 0)}
x, y = 0, 0
for m_dir, size in moves:
    x, y = x + moves_dir[m_dir][0] * size, y + moves_dir[m_dir][1] * size

print(x, y)