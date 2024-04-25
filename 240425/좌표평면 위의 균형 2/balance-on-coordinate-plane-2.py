N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
x_lst, y_lst = sorted(list(list(zip(*points))[0])), sorted(list(list(zip(*points))[1]))

mid_point = ((x_lst[0] + x_lst[-1]) // 2, (y_lst[0] + y_lst[-1]) // 2)

four_areas = [[] for _ in range(4)]

for x, y in points:
    if x < mid_point[0] and y > mid_point[1]:
        four_areas[0].append((x, y))
    elif x < mid_point[0] and y < mid_point[1]:
        four_areas[1].append((x, y))
    elif x > mid_point[0] and y < mid_point[1]:
        four_areas[2].append((x, y))
    elif x > mid_point[0] and y > mid_point[1]:
        four_areas[3].append((x, y))

four_areas = sorted(four_areas, key = lambda x: len(x), reverse = True)
print(len(four_areas[0]))