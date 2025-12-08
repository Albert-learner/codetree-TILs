n, q = map(int, input().split())

points = [tuple(map(int, input().split())) for _ in range(n)]
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
from bisect import bisect_left, bisect_right

ys = [y for _, y in points]
ys_sorted = sorted(set(ys))

def compress_y(y):
    return bisect_left(ys_sorted, y) + 1

points = [(x, compress_y(y)) for (x, y) in points]
points.sort() 

class BIT:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (n + 1)

    def add(self, i, v):
        while i <= self.n:
            self.t[i] += v
            i += i & -i

    def prefix_sum(self, i):
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s

    def range_sum(self, l, r):
        if l > r:
            return 0
        return self.prefix_sum(r) - self.prefix_sum(l - 1)

ny = len(ys_sorted)
bit = BIT(ny)

subqueries = []
answers = [0] * q

for idx, (x1, y1, x2, y2) in enumerate(queries):
    l = bisect_left(ys_sorted, y1)
    r = bisect_right(ys_sorted, y2) - 1
    if l > r:
        continue

    ly = l + 1
    ry = r + 1

    subqueries.append((x2, ly, ry, +1, idx))

subqueries.sort(key=lambda x: x[0])

p_idx = 0
num_points = len(points)

for T, ly, ry, sign, qi in subqueries:
    while p_idx < num_points and points[p_idx][0] <= T:
        _, cy = points[p_idx]
        bit.add(cy, 1)
        p_idx += 1

    cnt = bit.range_sum(ly, ry)
    answers[qi] += sign * cnt

print("\n".join(map(str, answers)))
