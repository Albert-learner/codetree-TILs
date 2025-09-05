n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from itertools import combinations

dist2 = [[0] * n for _ in range(n)]
for i in range(n):
    x1, y1 = points[i]
    for j in range(i + 1, n):
        x2, y2 = points[j]
        d2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        dist2[i][j] = dist2[j][i] = d2

best = float("inf")
for comb in combinations(range(n), m):
    cur_max = 0
    for a_i in range(m):
        ai = comb[a_i]
        for b_i in range(a_i+1, m):
            bi = comb[b_i]
            d2 = dist2[ai][bi]
            if d2 > cur_max:
                cur_max = d2
                if cur_max >= best:
                    break
        else:
            continue
        break
    if cur_max < best:
        best = cur_max

print(best)