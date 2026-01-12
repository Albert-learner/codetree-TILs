n, m = map(int, input().split())
points = list(map(int, input().split()))
segments = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
from bisect import bisect_left, bisect_right

points.sort()

out = []
for x, y in segments:
    if x > y:
        x, y = y, x

    left = bisect_left(points, x)
    right = bisect_right(points, y)
    out.append(str(right - left))

print("\n".join(out))