n, q = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
for x1, y1, x2, y2 in queries:
    sat_points = 0
    for x, y in points:
        if x1 <= x <= x2 and y1 <= y <= y2:
            sat_points += 1

    print(sat_points)