N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def check_positive(x1, y1, x2, y2):
    for x in range(x1, x2 + 1):
        for y in range(y1, y2 + 1):
            if board[x][y] <= 0:
                return False

    return True

def rect_size(x1, y1, x2, y2):
    size = 0

    if check_positive(x1, y1, x2, y2):
        rectangle = [board[i][j] for i in range(x1, x2 + 1) for j in range(y1, y2 + 1)]
        size = len(rectangle)

    return size

max_areas = 0
for i in range(N):
    for j in range(M):
        for h in range(N):
            for w in range(M):
                if rect_size(i, j, h, w) >= max_areas:
                    max_areas = rect_size(i, j, h, w)

if max_areas == 0:
    max_areas = -1

print(max_areas)