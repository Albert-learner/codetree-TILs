n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq as hq

pq = []
for elem in arr:
    hq.heappush(pq, -elem)

while m > 0:
    pq[0] += 1

    hq.heapify(pq)
    m -= 1

print(-pq[0])