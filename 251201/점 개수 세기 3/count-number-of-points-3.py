n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
sat_points = 0

for x, y in queries:
    if x == y:
        for point in points:
            if point == x:
                sat_points += 1
    else:
        for point in points:
            if point in set(range(x, y)):
                sat_points += 1

    print(sat_points)