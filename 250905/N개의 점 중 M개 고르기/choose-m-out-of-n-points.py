n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from itertools import combinations

point_combs = list(combinations(points, 2))
point_combs.sort(key=lambda x: (x[0][0] - x[1][0]) ** 2 + (x[0][1] - x[1][1]) ** 2)

dists = (point_combs[0][0][0] - point_combs[0][1][0]) ** 2 + (point_combs[0][0][1] - point_combs[0][1][1]) ** 2
print(dists)