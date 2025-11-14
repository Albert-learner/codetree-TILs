n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq as hq

pq = []
for elem in arr:
    hq.heappush(pq, -elem)

for _ in range(m):
    x = hq.heappop(pq)  
    x += 1               
    hq.heappush(pq, x)   

print(-pq[0])