areas = [[0] * 2001 for _ in range(2001)]

for s_idx in range(3):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 1000
    y1 += 1000
    x2 += 1000
    y2 += 1000

    for row in range(x1, x2):
        for col in range(y1, y2):
            areas[row][col] = 1 if s_idx != 2 else 0
    

cnts = 0
for row in range(len(areas)):
    for col in range(len(areas[0])):
        if areas[row][col]:
            cnts += 1

print(cnts)