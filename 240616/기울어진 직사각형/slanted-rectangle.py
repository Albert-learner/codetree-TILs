N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

mv_dirs = {1: (-1, 1), 2: (-1, -1), 3: (1, -1), 4: (1, 1)}

def in_range(mx, my):
    return 0 <= mx < N and 0 <= my < N

def get_score(x, y, w, h):
    move_size = [w, h, w, h]

    total = 0
    for (dx, dy), length in zip(mv_dirs.values(), move_size):
        for _ in range(length):
            x += dx
            y += dy

            if not in_range(x, y):
                return 0
            
            total += board[x][y]

    return total

max_sum = 0
for i in range(N):
    for j in range(N):
        for w in range(1, N):
            for h in range(1, N):
                max_sum = max(max_sum, get_score(i, j, w, h))

print(max_sum)