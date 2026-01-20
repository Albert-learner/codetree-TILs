n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
segments.sort()

def can_place(d: int) -> bool:
    last = -10**30
    for l, r in segments:
        x = max(l, last + d)
        if x > r:
            return False
        last = x

    return True

min_l = min(l for l, r in segments)
max_r = max(r for l, r in segments)
lo, hi = 0, max_r - min_l + 1

while lo + 1 < hi:
    mid = (lo + hi) // 2
    if can_place(mid):
        lo = mid
    else:
        hi = mid

print(lo)