areas = [[0] * 2001 for _ in range(2001)]
x1, y1, x2, y2 = map(lambda x: int(x) + 1000, input().split())
xx1, yy1, xx2, yy2 = map(lambda x: int(x) + 1000, input().split())

# 첫번째 사각형
for i in range(x1, x2):
    for j in range(y1, y2):
        areas[i][j] = 1

# 두번째 사각형
for i in range(xx1, xx2):
    for j in range(yy1, yy2):
        areas[i][j] = 0

min_x, max_x, min_y, max_y = len(areas), 0, len(areas[0]), 0
for i in range(x1, x2 + 1):
    for j in range(y1, y2 + 1):
        if areas[i][j] == 1:
            min_x = min(min_x, i)
            min_y = min(min_y, j)
            max_x = max(max_x, i)
            max_y = max(max_y, j)

print((max_x - min_x + 1) * (max_y - min_y + 1) if (min_x, min_y, max_x, max_y) != (2001, 2001, 0, 0) else 0)