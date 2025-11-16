n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

pq = []
first, second = 0, 0
for elem in arr:
    heapq.heappush(pq, -elem)

while len(pq) > 1:
    first = -heapq.heappop(pq) 
    second = -heapq.heappop(pq)
    if first != second:
        diff = first - second
        heapq.heappush(pq, -diff)

# 결과 처리
if len(pq) == 1:
    print(-pq[0])
else:
    print(-1)