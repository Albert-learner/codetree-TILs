N, T_max = map(int, input().split())
d = [int(input()) for _ in range(N)]

# Please write your code here.
import heapq

def can_finish(k: int) -> bool:
    pq = []
    first = min(k, N)
    for i in range(first):
        heapq.heappush(pq, d[i])

    for i in range(first, N):
        t = heapq.heappop(pq)
        t += d[i]
        if t > T_max:
            return False

        heapq.heappush(pq, t)

    return max(pq) <= T_max

lo, hi = 1, N
ans = N
while lo <= hi:
    mid = (lo + hi) // 2
    if can_finish(mid):
        ans = mid
        hi = mid - 1
    else:
        lo = mid + 1

print(ans)