n, m, k = map(int, input().split())

# Please write your code here.
from functools import lru_cache

INF = 10 ** 18
@lru_cache(None)
def cnts(pos : int, last : int, rem : int):
    if pos == n:
        return 1 if rem == 0 else 0

    needs_min = last * (n - pos)
    if rem < needs_min:
        return 0

    totals = 0
    vmax = rem // (n - pos)
    for v in range(last, vmax + 1):
        totals += cnts(pos + 1, v, rem - v)
        if totals >= INF:
            return INF

    return totals

ans = []
pos, last, rem = 0, 1, m
while pos < n:
    vmax = rem // (n - pos)
    for v in range(last, vmax + 1):
        c = cnts(pos + 1, v, rem - v)
        if k > c:
            k -= c
        else:
            ans.append(v)
            pos += 1
            rem -= v
            last = v
            break

print(*ans)