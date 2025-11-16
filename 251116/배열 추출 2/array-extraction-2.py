n = int(input())
x = [int(input()) for _ in range(n)]

# Please write your code here.
import heapq

pq = []
for elem in x:
    if elem != 0:
        heapq.heappush(pq, (int(abs(elem)), elem))
    else:
        if len(pq) != 0:
            _, ans = heapq.heappop(pq)
            print(ans)
        else:
            print(0)
