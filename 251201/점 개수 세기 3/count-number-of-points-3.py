n, q = map(int, input().split())
points = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
import bisect

points.sort()

for x, y in queries:
    left = bisect.bisect_left(points, x)
    right = bisect.bisect_right(points, y)

    sat_points = right - left
    print(sat_points)