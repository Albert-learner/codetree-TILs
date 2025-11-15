n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
import heapq

heap = []
for x, y in points:
    heapq.heappush(heap, (x + y, x, y))

for _ in range(m):
    d, x, y = heapq.heappop(heap)
    x += 2
    y += 2
    heapq.heappush(heap, (x + y, x, y))

_, x, y = heap[0]
print(x, y)