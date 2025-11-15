n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import deque

points.sort(lambda x: ((x[0] + x[1]), (x[0], x[1])))
points = deque(points)

while m > 0:
    cx, cy = points.popleft()
    cx += 2
    cy += 2
    points.appendleft((cx, cy))
    points = list(points)
    points.sort(lambda x: ((x[0] + x[1]), (x[0], x[1])))
    points = deque(points)
    m -= 1

print(points[0][0], points[0][1])