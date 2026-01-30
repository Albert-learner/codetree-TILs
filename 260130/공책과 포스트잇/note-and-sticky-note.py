N, K, L = map(int, input().split())
c = list(map(int, input().split()))

# Please write your code here.
import heapq

total_slots = K * L

def can_make(h: int) -> bool:
    if h == 0:
        return True

    already = 0
    deficits = []

    for ci in c:
        if ci >= h:
            already += 1
        else:
            d = h - ci
            if d <= K:
                deficits.append(d)

    need = h - already
    if need <= 0:
        return True
    if len(deficits) < need:
        return False

    smallest = heapq.nsmallest(need, deficits)
    return sum(smallest) <= total_slots

lo, hi = 0, N
ans = 0
while lo <= hi:
    mid = (lo + hi) // 2
    if can_make(mid):
        ans = mid
        lo = mid + 1
    else:
        hi = mid - 1

print(ans)