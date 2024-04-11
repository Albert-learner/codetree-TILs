N = int(input())

areas = [[0] * 201 for _ in range(201)]
for r_idx in range(N):
    x1, y1, x2, y2 = map(lambda x: int(x) + 100, input().split())

    if r_idx % 2 == 0:
        for i in range(x1, x2):
            for j in range(y1, y2):
                areas[i][j] = 'R'
    else:
        for i in range(x1, x2):
            for j in range(y1, y2):
                areas[i][j] = 'B'

blue_cnts = 0
for row in range(len(areas)):
    for col in range(len(areas[0])):
        if areas[row][col] == 'B':
            blue_cnts += 1

print(blue_cnts)