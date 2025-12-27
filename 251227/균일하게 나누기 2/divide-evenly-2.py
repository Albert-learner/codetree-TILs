n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
MAXY = 1001

left = [0] * (MAXY + 1)
right = [0] * (MAXY + 1)

for x, y in points:
    right[y] += 1

points.sort()

def evaluate():
    total_left = sum(left)
    total_right = sum(right)

    pl = [0] * (MAXY + 1)
    pr = [0] * (MAXY + 1)
    runl = runr = 0
    for y in range(MAXY + 1):
        runl += left[y]
        runr += right[y]
        pl[y] = runl
        pr[y] = runr

    best = 10 ** 18
    for b in range(2, 1001, 2):
        below_y = b - 1

        lb = pl[below_y]
        la = total_left - lb
        rb = pr[below_y]
        ra = total_right - rb

        best = min(best, max(lb, la, rb, ra))

    return best

ans = evaluate()

i = 0
while i < n:
    cur_x = points[i][0]

    while i < n and points[i][0] == cur_x:
        _, y = points[i]
        right[y] -= 1
        left[y] += 1
        i += 1

    ans = min(ans, evaluate())

print(ans)