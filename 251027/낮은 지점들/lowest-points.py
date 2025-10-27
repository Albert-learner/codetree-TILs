n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from collections import defaultdict

grouped_points = defaultdict(list)
for x, y in points:
    grouped_points[x].append((x, y))

min_y_sum = 0
for x in grouped_points:
    min_y = min(y for _, y in grouped_points[x])
    min_y_sum += min_y

print(min_y_sum)