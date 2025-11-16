n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

pq = []
for elem in arr:
    heapq.heappush(pq, -elem)

while len(pq) >= 2:
    if pq[0] != pq[1]:
        first, second = heapq.heappop(pq), heapq.heappop(pq)
        diff = int(abs(first)) - int(abs(second))
        heapq.heappush(pq, -diff)
    else:
        heapq.heappop(pq)
        heapq.heappop(pq)
    
    heapq.heapify(pq)

print(int(abs(pq[0])))
    
