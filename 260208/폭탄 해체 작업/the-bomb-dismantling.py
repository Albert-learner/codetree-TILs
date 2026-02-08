N = int(input())
bombs = [tuple(map(int, input().split())) for _ in range(N)]

# Please write your code here.
import heapq

bombs.sort(key = lambda x: x[1])

pq, total = [], 0

for score, time_limit in bombs:
    heapq.heappush(pq, score)
    total += score

    if len(pq) > time_limit:
        total -= heapq.heappop(pq)

print(total)