N = int(input())
squares = [list(map(lambda x: int(x) + 100, input().split())) for _ in range(N)]

areas = [[0] * 201 for _ in range(201)]
for x, y in squares:
    for row in range(x, x + 8):
        for col in range(y, y + 8):
            areas[row][col] = 1

cnts = 0
for row in range(len(areas)):
    for col in range(len(areas[0])):
        if areas[row][col] == 1:
            cnts += 1

print(cnts)