n = int(input())
r1, c1, r2, c2 = map(int, input().split())

# Please write your code here.
from collections import deque

from collections import deque

dists = [[0] * (n + 1) for _ in range(n + 1)]
que = deque()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def check_move(x, y):
    return in_range(x, y) and not dists[x][y]

def BFS():
    while que:
        x, y, step = que.popleft()

        if x == r2 and y == c2:
            return step

        knight_moves = {(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                        (1, -2), (1, 2), (2, -1), (2, 1)}

        for dx, dy in knight_moves:
            mx, my = x + dx, y + dy
            if check_move(mx, my):
                dists[mx][my] = 1
                que.append((mx, my, step + 1))

    return step

que.append((r1, c1, 0))
dists[r1][c1] = 1
total_moves = BFS()

if dists[r2][c2] == 0:
    print(-1)
else:
    print(total_moves)

