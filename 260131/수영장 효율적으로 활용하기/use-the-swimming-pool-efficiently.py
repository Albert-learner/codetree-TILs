n, m = map(int, input().split())
T = list(map(int, input().split()))

# Please write your code here.
def can(limit: int) -> bool:
    cnt, cur = 1, 0
    for x in T:
        if cur + x <= limit:
            cur += x
        else:
            cnt += 1
            cur = x
            if cnt > m:
                return False

    return True

lo, hi = max(T), sum(T)
ans = hi

while lo <= hi:
    mid = (lo + hi) // 2
    if can(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)