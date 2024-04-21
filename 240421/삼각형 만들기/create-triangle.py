N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]

def is_parallel(p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    if (x1 == x2 or x2 == x3 or x3 == x1) and (y1 == y2 or y2 == y3 or y3 == y1):
        return True
    else:
        return False

max_areas = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            first, second, third = coords[i], coords[j], coords[k]

            if is_parallel(first, second, third):
                x1, y1 = first
                x2, y2 = second
                x3, y3 = third

                x_min = min(x1, x2, x3)
                x_max = max(x1, x2, x3)
                y_min = min(y1, y2, y3)
                y_max = max(y1, y2, y3)

                diff = ((x_max - x_min) * (y_max - y_min))
                max_areas = max(max_areas, diff)

print(max_areas)