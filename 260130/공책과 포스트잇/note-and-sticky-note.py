import sys
import heapq

input = sys.stdin.readline

N, K, L = map(int, input().split())
c = list(map(int, input().split()))

total_slots = K * L  # 총 추가로 적을 수 있는 횟수

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
            if d <= K:          # 한 공책은 포스트잇 K장에 최대 K번까지만 적을 수 있음
                deficits.append(d)

    need = h - already
    if need <= 0:
        return True
    if len(deficits) < need:
        return False

    # need개를 가장 적은 증가량부터 선택
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
