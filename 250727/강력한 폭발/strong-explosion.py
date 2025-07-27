n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import copy

bomb_places = [(i, j) for i in range(n) for j in range(n) if grid[i][j] == 1]

max_bombs = 0

def execute(cnts, grid):
    global max_bombs

    if cnts == len(bomb_places):
        matrix = copy.deepcopy(grid)
        bomb(matrix)
        max_bombs = max(max_bombs, count(matrix))
        return

    x, y = bomb_places[cnts]

    for i in range(1, 4):
        grid[x][y] = i
        execute(cnts + 1, grid)
        grid[x][y] = 1

def bomb(matrix):
    N = len(matrix)
    to_bomb = []

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                to_bomb.append((i, j))
                for d in range(1, 3):
                    if 0 <= i - d:
                        to_bomb.append((i - d, j))
                    if i + d < n:
                        to_bomb.append((i + d, j))
            elif matrix[i][j] == 2:
                to_bomb.extend([
                    (i, j),
                    (i - 1, j) if i - 1 >= 0 else None,
                    (i + 1, j) if i + 1 < n else None,
                    (i, j - 1) if j - 1 >= 0 else None,
                    (i, j + 1) if j + 1 < n else None
                ])
            elif matrix[i][j] == 3:
                to_bomb.extend([
                    (i, j),
                    (i - 1, j - 1) if i - 1 >= 0 and j - 1 >= 0 else None,
                    (i - 1, j + 1) if i - 1 >= 0 and j + 1 < n else None,
                    (i + 1, j - 1) if i + 1 < n and j - 1 >= 0 else None,
                    (i + 1, j + 1) if i + 1 < n and j + 1 < n else None
                ])

    for pos in to_bomb:
        if pos:
            x, y = pos
            matrix[x][y] = -1

def count(matrix):
    return sum(row.count(-1) for row in matrix)

execute(0, grid)
print(max_bombs)