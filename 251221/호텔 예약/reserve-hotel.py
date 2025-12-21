n = int(input())
intervals = [tuple(map(int, input().split())) for _ in range(n)]
s = [interval[0] for interval in intervals]
e = [interval[1] for interval in intervals]

# Please write your code here.
import heapq

jobs = sorted(zip(s, e))

heap = []
ans = 0

for start, end in jobs:
    while heap and heap[0] < start:
        heapq.heappop(heap)

    heapq.heappush(heap, end)
    if len(heap) > ans:
        ans = len(heap)

print(ans)