n, m = map(int, input().split())
fires = list(map(int, input().split()))
stations = list(map(int, input().split()))

# Please write your code here.
from bisect import bisect_left

stations.sort()

ans = 0
INF = 10 ** 30

for x in fires:
    idx = bisect_left(stations, x)

    best = INF
    if idx < m:
        best = min(best, abs(stations[idx] - x))
    if idx > 0:
        best = min(best, abs(stations[idx - 1] - x))

    ans = max(ans, best)

print(ans)