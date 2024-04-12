N = int(input())
pos = [0, 0]
move_dirs = {'N': [1, 0], 'S': [-1, 0], 'W': [0, -1], 'E': [0, 1]}

for _ in range(N):
    mv_dir, dist = input().split()
    dist = int(dist)
    total_move = [move_dirs[mv_dir][0] * dist, move_dirs[mv_dir][1] * dist]
    pos = [pos[0] + total_move[0], pos[1] + total_move[1]]
    
print(*pos[::-1])