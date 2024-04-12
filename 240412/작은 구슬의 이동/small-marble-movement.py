N, T = map(int, input().split())
marble_x, marble_y, mv_dir = input().split()
marble_x, marble_y = int(marble_x) - 1, int(marble_y) - 1

move_dirs = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

while T > 0:
    if marble_x in range(N) and marble_y in range(N):
        if marble_x + move_dirs[mv_dir][0] in range(N) and marble_y + move_dirs[mv_dir][1] in range(N):
            marble_x, marble_y = marble_x + move_dirs[mv_dir][0], marble_y + move_dirs[mv_dir][1]
        else:
            if mv_dir == 'L':
                mv_dir = 'R'
            elif mv_dir == 'R':
                mv_dir = 'L'
            elif mv_dir == 'U':
                mv_dir = 'D'
            elif mv_dir == 'D':
                mv_dir = 'U'

    T -= 1

print(marble_x + 1, marble_y + 1)