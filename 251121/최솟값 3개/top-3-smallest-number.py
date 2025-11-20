n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
import heapq

pq = []
for elem in arr:
    heapq.heappush(pq, elem)

    if len(pq) < 3:
        print(-1)
    else:
        mul = 1
        for sub_elem in pq[:3]:
            mul *= sub_elem

        print(mul)