N = int(input())
move_dirs = {'N': (1, 0), 'S': (-1, 0), 'W': (0, -1), 'E': (0, 1)}
coords = []
x, y = 0, 0

answer, times = 0, 0
for _ in range(N):
    mv_dir, size = input().split()
    size = int(size)

    for _ in range(size):
        x, y = x + move_dirs[mv_dir][0], y + move_dirs[mv_dir][1]
        if (x, y) == (0, 0):
            times += 1
            coords.append((x, y))
            answer += times
            break
        else:
            coords.append((x, y))

        times += 1

if (0, 0) not in coords:
    answer = -1
    
print(answer)