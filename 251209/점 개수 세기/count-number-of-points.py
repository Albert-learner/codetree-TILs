n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
from bisect import bisect_left, bisect_right

points.sort()
for x, y in queries:
    left = bisect_left(points, x)
    right = bisect_right(points, y)

    sat_points = right - left
    print(sat_points)