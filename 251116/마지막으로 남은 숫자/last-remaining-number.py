n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

pq = []
first, second = 0, 0
for elem in arr:
    heapq.heappush(pq, -elem)

while len(pq) >= 2:
    first, second = heapq.heappop(pq), heapq.heappop(pq)
    if first != second:
        diff = int(abs(first)) - int(abs(second))
        heapq.heappush(pq, -diff)
    else:
        first = heapq.heappop(pq)
        second = heapq.heappop(pq)
    
    heapq.heapify(pq)

print(int(abs(first)) - int(abs(second)))
    
