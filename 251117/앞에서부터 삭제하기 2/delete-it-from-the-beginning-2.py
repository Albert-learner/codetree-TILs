n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

pq = []
for k in range(1, n - 2):
    max_avg = 0
    for elem in arr[k:]:
        heapq.heappush(pq, elem)
    
    avg = sum(pq[1:]) / (len(pq) - 1)
    max_avg = max(max_avg, avg)
    pq = []

print("{:.2f}".format(max_avg))
    