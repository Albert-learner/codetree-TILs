C, N = map(int, input().split())
T = [int(input()) for _ in range(C)]
AB = [tuple(map(int, input().split())) for _ in range(N)]
A = [ab[0] for ab in AB]
B = [ab[1] for ab in AB]

# Please write your code here.
import heapq

T.sort()
AB.sort(key = lambda x: x[0])

pq = []
j, ans = 0, 0

for t in T:
    while j < N and AB[j][0] <= t:
        heapq.heappush(pq, AB[j][1])
        j += 1

    while pq and pq[0] < t:
        heapq.heappop(pq)

    if pq:
        heapq.heappop(pq)
        ans += 1

print(ans)