N, M, R, C = map(int, input().split())
R, C = R - 1, C - 1

bombs = set()
bombs.add((R, C))

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

for t in range(1, M + 1):
    dsts = 2 ** (t - 1)
    new_bombs = set()
    for x, y in bombs:
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            mx, my = x + dsts * dx, y + dsts * dy
            if in_range(mx, my):
                new_bombs.add((mx, my))

    bombs = bombs.union(new_bombs)

print(len(bombs))