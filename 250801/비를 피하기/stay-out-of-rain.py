n, h, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

dists = [[0] * n for _ in range(n)]

def find_people_location():
    people_poses = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                people_poses.append((i, j))

    return people_poses

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def BFS():
    moves = {(-1, 0), (1, 0), (0, -1), (0, 1)}

    while que:
        x, y, value = que.popleft()

        for dx, dy in moves:
            mx, my = x + dx, y + dy
            if in_range(mx, my) and not visited[mx][my] and grid[mx][my] != 1:
                visited[mx][my] = True

                if grid[mx][my] != 3:
                    que.append((mx, my, value + 1))
                else:
                    return value + 1

    return -1

people = find_people_location()
for person in people:
    x, y = person

    que = deque([(x, y, 0)])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True

    dists[x][y] = BFS()

for row in dists:
    print(*row)