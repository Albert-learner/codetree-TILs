n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
import heapq

pq = []
for num in x:
    if num > 0:
        heapq.heappush(pq, num)
    elif num == 0:
        if len(pq) != 0:
            print(heapq.heappop(pq))
        else:
            print(0)
