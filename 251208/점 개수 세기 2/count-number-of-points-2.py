n, q = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
for x1, y1, x2, y2 in queries:
    x_set = set(range(x1, x2 + 1))
    y_set = set(range(y1, y2 + 1))

    sat_points = 0
    for x, y in points:
        if x in x_set and y in y_set:
            sat_points += 1

    print(sat_points)