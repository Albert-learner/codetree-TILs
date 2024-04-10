N = int(input())
rectangles = [list(map(int, input().split())) for _ in range(N)]

total_areas = 0
overlap_areas = (min(list(zip(*rectangles))[2]) - max(list(zip(*rectangles))[0])) * (min(list(zip(*rectangles))[3]) - max(list(zip(*rectangles))[1]))
for x1, y1, x2, y2 in rectangles:
    area = (x2 - x1) * (y2 - y1)
    total_areas += area

total_areas -= overlap_areas
print(total_areas)