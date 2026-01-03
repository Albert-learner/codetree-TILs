n, d = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
from collections import deque

points.sort()
xs = [p[0] for p in points]
ys = [p[1] for p in points]

minq = deque()  
maxq = deque() 

ans = float('inf')
l = 0

for r in range(n):
    while minq and ys[minq[-1]] >= ys[r]:
        minq.pop()
    minq.append(r)

    while maxq and ys[maxq[-1]] <= ys[r]:
        maxq.pop()
    maxq.append(r)

    while l <= r and ys[maxq[0]] - ys[minq[0]] >= d:
        ans = min(ans, xs[r] - xs[l])

        if minq and minq[0] == l:
            minq.popleft()
        if maxq and maxq[0] == l:
            maxq.popleft()
        l += 1

print(-1 if ans == float('inf') else ans)